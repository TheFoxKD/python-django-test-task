from django.urls import path

from ..views import shop_views as views

app_name = 'shops'
urlpatterns = [
    path('', views.ShopListView.as_view(), name='list'),
    path('<int:pk>/', views.ShopDetailView.as_view(), name='detail'),
    path('create/', views.ShopCreateView.as_view(), name='create'),
]
