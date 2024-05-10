from django.urls import path

from ..views import shop_views as views

app_name = 'shop'
urlpatterns = [
    path('', views.ShopListView.as_view(), name='list'),
    path('<int:shop_id>/', views.ShopDetailView.as_view(), name='detail'),

]
