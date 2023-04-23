from django.contrib import admin

from webtoon.models import WebtoonModel
from webtoon.models import TagModel
from webtoon.models import AutherModel
from webtoon.models import DayModel
from webtoon.models import BookmarkModel



@admin.register(WebtoonModel)
class WebtoonAdmin(admin.ModelAdmin):
    """
    웹툰 관리자
    """
    list_display = (
        'webtoon_name',
        'webtoon_img',
        'get_auther',
        'get_tag',
        'webtoon_end',
        'webtoon_adult',
    )
    list_filter = (
        'webtoon_end',
        'webtoon_adult',
    )
    search_fields = (
        'webtoon_name',
    )


@admin.register(AutherModel)
class AutherAdmin(admin.ModelAdmin):
    """
    작가 관리자
    """
    list_display = (
        'auther_name',
    )
    list_filter = (
        'auther_name',
    )


@admin.register(DayModel)
class DayAdmin(admin.ModelAdmin):
    """
    연재일 관리자
    """
    list_display = (
        'day_name',
    )
    list_filter = (
        'day_name',
    )

@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    """
    태그 관리자
    """
    list_display = (
        'tag_name',
    )
    list_filter = (
        'tag_name',
    )


@admin.register(BookmarkModel)
class BookmarkAdmin(admin.ModelAdmin):
    """
    태그 관리자
    """
    list_display = (
        'user_info',
        'get_bookmark',
    )
