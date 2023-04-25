from django.core.files.storage import FileSystemStorage
from django.db import models
from django.conf import settings

# 웹툰 파일명으로 이미지 저장
def webtoon_img_path(instance, filename):
    """웹툰 파일명으로 이미지 저장"""
    # Rename the file to its name.
    return 'webtoon/{0}.jpg'.format(instance.webtoon_name)

# 파일저장시 관리 클래스
class OverwriteStorage(FileSystemStorage):
    """파일저장시 관리 클래스"""
    def get_available_name(self, name, max_length=None):
        """이미 있는 파일의 경우 삭제후 저장"""
        # If the file already exists, delete it so it can be replaced.
        print(self, name, max_length)
        if self.exists(name):
            self.delete(name)
        return name

# 작가 테이블
class AutherModel(models.Model):
    """
    작가 모델
    id : pk 값
    auther_name : 이름
    auther_create_time : 생성일
    """
    class Meta:
        app_label = 'webtoon'
        verbose_name = '작가'
        verbose_name_plural = '작가 리스트'

    auther_name = models.CharField(
        max_length=20,
        verbose_name='이름',
    )
    auther_create_time = models.DateTimeField(
        verbose_name='생성일',
        auto_now_add=True,
    )
    def __str__(self,) -> str:
        return format(self.auther_name)

# 연재일 테이블
class DayModel(models.Model):
    """ 
    연재일 모델 
    id : pk 값
    day_name : 연재일
    day_create_time : 생성일
    """
    class Meta:
        app_label = 'webtoon'
        verbose_name = '연재일'
        verbose_name_plural = '연재일 리스트'

    day_name = models.CharField(
        max_length=3,
        verbose_name='연재일',
    )
    day_create_time = models.DateTimeField(
        verbose_name='생성일',
        auto_now_add=True,
    )

    def __str__(self,) -> str:
        return format(self.day_name)

# 태그 테이블
class TagModel(models.Model):
    """
    태그 모델
    id : pk 값
    tag_name : 태그 명
    tag_create_time : 태그 생성일
    WebtoonModels_set : 웹툰과 n:m 관계
    """
    class Meta:
        app_label = 'webtoon'
        verbose_name = '태그'
        verbose_name_plural = '태그 리스트'

    tag_name = models.CharField(
        max_length=10,
        verbose_name='태그',
        unique=True,
    )
    tag_create_time = models.DateTimeField(
        verbose_name='생성일',
        auto_now_add=True,
    )

    def __str__(self,) -> str:
        return format(self.tag_name)

# 웹툰 테이블
class WebtoonModel(models.Model):
    """
    웹툰 모델
    id : pk 값
    webtoon_name : 웹툰
    webtoon_description : 설명
    webtoon_tag : 태그
    webtoon_auther : 작가
    webtoon_link : 링크
    webtoon_img : 이미지
    webtoon_end : 완결여부 True:완결, False:연재(default)
    webtoon_day : 연재일
    webtoon_adult : 성인여부  True:성인, False:전체(default)
    webtoon_create_time :생성일   
    """
    class Meta:
        app_label = 'webtoon'
        verbose_name = '웹툰'
        verbose_name_plural = '웹툰 리스트'

    webtoon_name = models.CharField(
        max_length=100,
        verbose_name='웹툰',
        unique=True,
    )
    webtoon_description = models.CharField(
        max_length=1000,
        verbose_name='설명',
        null=True,
        blank=True,
    )
    webtoon_tag = models.ManyToManyField(
        TagModel,
        verbose_name='태그',
        blank=True,
    )
    webtoon_auther = models.ManyToManyField(
        AutherModel,
        verbose_name='작가',
        blank=True,
    )
    webtoon_link = models.CharField(
        max_length=500,
        verbose_name='링크',
        null=True,
        blank=True,
    )
    webtoon_img = models.ImageField(
        upload_to=webtoon_img_path,
        storage=OverwriteStorage,
        verbose_name='이미지',
        null=True,
        blank=True,
    )
    webtoon_end = models.BooleanField(
        verbose_name='완결',
        default=False,
    )
    webtoon_day = models.ForeignKey(
        'DayModel',
        verbose_name='연재일',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    webtoon_adult = models.BooleanField(
        verbose_name='성인',
        default=False,
    )
    webtoon_create_time = models.DateTimeField(
        verbose_name='생성일',
        auto_now_add=True,
    )


    def __str__(self,) -> str:
        return format(self.webtoon_name)

    def get_auther(self,) -> str:
        return ", ".join([obj.auther_name for obj in self.webtoon_auther.all()])
    get_auther.short_description = '작가'

    def get_tag(self,) -> str:
        return ", ".join([obj.tag_name for obj in self.webtoon_tag.all()])
    get_tag.short_description = '태그'

    def get_image_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.webtoon_img)


class BookmarkModel(models.Model):
    """
    유저별 북마크 모델
    id : pk 값
    user_info : 유저uuid명
    bookmark_webtoon : 유저와 웹툰 n:m
    user_create_time : 생성일자
    """
    class Meta:
        app_label = 'webtoon'
        verbose_name = '북마크'
        verbose_name_plural = '유저별 북마크'

    user_info = models.CharField(
        max_length=255,
        verbose_name='유저식별값'
    )
    bookmark_webtoon = models.ManyToManyField(
        WebtoonModel,
        verbose_name='북마크',
        blank=True,
    )
    user_create_time = models.DateTimeField(
        verbose_name='생성일',
        auto_now_add=True,
    )

    def __str__(self,) -> str:
        return format(self.user_info)

    def get_bookmark(self,) -> str:
        return ", ".join([obj.webtoon_name for obj in self.bookmark_webtoon.all()])

    get_bookmark.short_description = '북마크 목록'
