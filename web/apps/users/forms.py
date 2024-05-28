from typing import override

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .exceptions import AuthenticationException
from .repository import UserRepository
from .services import UserService

user_service = UserService(UserRepository())

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if '@' in username:
            raise forms.ValidationError('Username should not contain "@"')

        return super().clean_username()

    @override
    def save(self, commit=True):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')

        user: User = user_service.register_user(username=username, email=email, password=password)
        return user


class CustomAuthenticationForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')

        if username_or_email is None or password is None:
            raise forms.ValidationError('Empty username or password')

        try:
            user: User = user_service.authenticate_user(username_or_email, password)
        except AuthenticationException as exception:
            raise forms.ValidationError(exception.message)
        else:
            self.cleaned_data['user'] = user

        return self.cleaned_data

    def get_user(self) -> User:
        return self.cleaned_data.get('user')
