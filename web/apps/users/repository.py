from typing import override

from django.contrib.auth import get_user_model

from .interfaces import IUserRepository

User = get_user_model()


class UserRepository(IUserRepository):
    @override
    def create_user(self, username: str, email: str, password: str) -> User:
        return User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

    @override
    def username_exists(self, username: str) -> bool:
        return User.objects.filter(username=username).exists()
