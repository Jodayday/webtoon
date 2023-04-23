

from django.urls import path
from django.shortcuts import redirect

from webtoon.views import WebtoonView
from webtoon.views import BookmarkView
from webtoon.views import bookmark_check


def index(request):
    return redirect('list/')


app_name = 'webtoon'

urlpatterns = [
    path('', index,),
    path('list/', WebtoonView.as_view(), name='list'),
    path('bookmark/', BookmarkView.as_view(), name='bookmark'),
    path('check/', bookmark_check, name='check',),
]
