# noinspection PyUnresolvedReferences
from .base import *

SECRET_KEY = 'my-secret-key'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_test_task_db',
        'USER': 'django_test_task_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
