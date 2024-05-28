from django.urls import path

from . import utils

app_name = 'utils'
urlpatterns = [
    path('check_username/', utils.check_username, name='check_username'),
    path('check_email/', utils.check_email, name='check_email')
]
