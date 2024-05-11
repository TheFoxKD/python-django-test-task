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
