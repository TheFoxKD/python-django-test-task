from dataclasses import dataclass

from django.contrib.auth import get_user_model

from .interfaces import IUserRepository

User = get_user_model()


@dataclass
class UserService:
    user_repository: IUserRepository

    def check_username_availability(self, username: str) -> bool:
        return not self.user_repository.username_exists(username=username)

    def register_user(self, username: str, email: str, password: str) -> User:
        user: User = self.user_repository.create_user(username=username, email=email, password=password)
        return user

    def authenticate_user(self, username_or_email: str, password: str) -> User:
        user = self.user_repository.get_user_by_username_or_email(username_or_email)

        if user is None:
            raise ValueError('User not found')

        if not user.check_password(password):
            raise ValueError('Invalid password')

        return user

    def check_email_availability(self, email: str) -> bool:
        return not self.user_repository.email_exists(email=email)
