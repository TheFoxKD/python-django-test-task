from abc import ABC, abstractmethod

from django.contrib.auth import get_user_model

User = get_user_model()


class IUserRepository(ABC):

    @abstractmethod
    def create_user(self, username: str, email: str, password: str) -> User:
        pass

    @abstractmethod
    def username_exists(self, username: str) -> bool:
        pass

    @abstractmethod
    def get_user_by_username_or_email(self, username_or_email: str) -> User | None:
        pass

    @abstractmethod
    def email_exists(self, email: str) -> bool:
        pass
