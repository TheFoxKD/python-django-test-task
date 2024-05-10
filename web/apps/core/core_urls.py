from django.urls import include, path

app_name = 'core'
urlpatterns = [
    path('shop/', include('web.apps.core.urls.shop_urls')),
]
