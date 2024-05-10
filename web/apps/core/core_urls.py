from django.urls import include, path

app_name = 'core'
urlpatterns = [
    path('shops/', include('apps.core.urls.shop_urls')),
]
