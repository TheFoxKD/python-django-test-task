from django.urls import path

from ..users import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
]