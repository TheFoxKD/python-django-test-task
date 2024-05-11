from typing import override

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import Q

from .interfaces import IUserRepository

User = get_user_model()


class UserRepository(IUserRepository):
    @override
    def create_user(self, username: str, email: str, password: str) -> User:
        if '@' in username:
            raise ValidationError("Username may not contain '@'")

        return User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

    @override
    def username_exists(self, username: str) -> bool:
        return User.objects.filter(username=username).exists()

    @override
    def get_user_by_username_or_email(self, username_or_email: str) -> User | None:
        return User.objects.filter(
            Q(username=username_or_email) | Q(email=username_or_email)
        ).first()

    @override
    def email_exists(self, email: str) -> bool:
        return User.objects.filter(email=email).exists()
