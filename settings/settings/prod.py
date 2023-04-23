from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# DOCKER SECRETS 사용
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': read_secret('MYSQL_DATABASE'),
        'USER': read_secret('MYSQL_USER'),
        'PASSWORD': read_secret('MYSQL_PASSWORD'),
        'HOST': 'mysql',
        'PORT': '3306',
    }
}