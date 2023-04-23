from .base import *
from .secret_key import SECRET_KEY_FILE
DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = SECRET_KEY_FILE

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}