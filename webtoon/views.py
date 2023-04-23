import uuid
from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic import View
from django.db.models import Q
from django.core.paginator import Paginator
from webtoon.models import WebtoonModel
from webtoon.models import AutherModel
from webtoon.models import DayModel
# from webtoon.models import PublishingModel
from webtoon.models import TagModel
from webtoon.models import BookmarkModel

# Create your views here.

from django.http import JsonResponse


class WebtoonView(ListView):
    model = WebtoonModel
    template_name = 'list.html'
    context_object_name = 'webtoon_list'
    paginate_by = 20  # 한 페이지에 보여줄 오브젝트의 갯수

    def get_context_data(self, **kwargs):
        # 추가적인 데이터(DB에 있는것)를 추가할때 사용
        context = super().get_context_data(**kwargs)

        # 연재일 데이터
        context['day_list'] = DayModel.objects.all()
        # 선택한 연재일
        context['day_select'] = self.request.GET.get('day')

        # 연재상태
        context['status'] = self.request.GET.get('status')

        # 태그 데이터
        context['tag_list'] = TagModel.objects.all()
        # 선택한 태그
        context['tag_select'] = self.request.GET.get('tag')

        context['search'] = self.request.GET.get('search')
        # 유저의 북마크 정보 표기
        user_info = self.request.COOKIES.get("user_info")
        if user_info:
            try:
                bookmark = BookmarkModel.objects.get(user_info=user_info)
            except BookmarkModel.DoesNotExist:
                context['user_info'] = list()
            else:
                context['user_info'] = bookmark.bookmark_webtoon.all()

        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        response = super().get(request, *args, **kwargs)
        # 첫 접속자의 경우 신규 id 발급
        if not request.COOKIES.get('user_info'):
            user_info = str(uuid.uuid4())
            response.set_cookie('user_info', user_info)
            BookmarkModel(
                user_info=user_info,
            ).save()

        return response

    def get_queryset(self):
        queryset = super().get_queryset()

        # url의 쿼리스트링 분석
        day = self.request.GET.get('day')
        status = self.request.GET.get('status')
        tag = self.request.GET.get('tag')
        search = self.request.GET.get('search')

        if status == "1":
            queryset = queryset.filter(webtoon_end=False,
                                       webtoon_adult=False)
        elif status == "2":
            queryset = queryset.filter(webtoon_end=False,
                                       webtoon_adult=True)
        elif status == "3":
            queryset = queryset.filter(webtoon_end=True)

        if day:
            if day != "0":
                dayM = DayModel.objects.get(day_name=day)
                queryset = queryset.filter(webtoon_day=dayM)
        if tag:
            if tag != "0":
                tagquery = TagModel.objects.get(pk=tag)
                queryset = queryset.filter(webtoon_tag=tagquery)

        if search:
            queryset = queryset.filter(
                Q(webtoon_name__icontains=search)).distinct()

        return queryset


class BookmarkView(ListView):
    model = BookmarkModel
    template_name = 'bookmark.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # 연재상태
        status = self.request.GET.get('status')
        context['status'] = status
        # 태그 데이터
        context['tag_list'] = TagModel.objects.all()
        # 선택한 태그
        tag_select = self.request.GET.get('tag')
        context['tag_select'] = tag_select

        # 유저 id를 통해 북마크 정보를 조회
        if user_info := self.request.COOKIES.get('user_info'):
            user, _ = BookmarkModel.objects.get_or_create(user_info=user_info)
            queryset = user.bookmark_webtoon.all()

            if status == "1":
                queryset = user.bookmark_webtoon.filter(webtoon_end=False,
                                                        webtoon_adult=False)
            elif status == "2":
                queryset = user.bookmark_webtoon.filter(webtoon_end=False,
                                                        webtoon_adult=True)
            elif status == "3":
                queryset = user.bookmark_webtoon.filter(
                    webtoon_end=True)
            else:
                queryset = user.bookmark_webtoon.all()

            if tag_select:
                if tag_select != '0':
                    tagquery = TagModel.objects.get(pk=tag_select)
                    queryset = queryset.filter(
                        webtoon_tag=tagquery)
                else:
                    queryset = queryset.all()
            else:
                queryset = user.bookmark_webtoon.all()

            # 검색
            if search := self.request.GET.get('search'):
                context['search'] = search
                queryset = queryset.filter(
                    Q(webtoon_name__icontains=search)).distinct()

            # 페이징
            if page_select := self.request.GET.get('page'):
                paginator = Paginator(queryset, 10)
                page_info = paginator.get_page(page_select)
                context['page_obj'] = page_info
                queryset = page_info.object_list

            context['bookmark'] = queryset
        return context


def bookmark_check(request):
    # 북마크 버튼 누를시 유저 id 에 북마크 기록 저장
    webtoon_id = request.POST.get("bookmark")
    user_info = request.COOKIES.get('user_info')
    method = request.POST.get("check")
    if webtoon_id and user_info:
        webtoon = WebtoonModel.objects.get(pk=webtoon_id)
        user = BookmarkModel.objects.get(user_info=user_info)
        if method == 'true':
            user.bookmark_webtoon.add(webtoon)
        else:
            user.bookmark_webtoon.remove(webtoon)
        user.save()
    return redirect(reverse('webtoon:list'))
