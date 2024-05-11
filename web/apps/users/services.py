from dataclasses import dataclass

from django.contrib.auth import get_user_model

from .interfaces import IUserRepository

User = get_user_model()


@dataclass
class UserService:
    user_repository: IUserRepository

    def check_username_availability(self, username: str) -> bool:
        return not self.user_repository.username_exists(username)

    def register_user(self, username: str, email: str, password: str) -> User:
        user: User = self.user_repository.create_user(username=username, email=email, password=password)
        return user
