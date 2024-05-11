from typing import override

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .repository import UserRepository
from .services import UserService

user_service = UserService(UserRepository())

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @override
    def save(self, commit=True):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        user: User = user_service.register_user(username=username, email=email, password=password)
        return user
