from abc import ABC, abstractmethod

from django.db.models import QuerySet

from web.apps.core.models import Shop


class IShopRepository(ABC):

    @abstractmethod
    def get_all(self) -> QuerySet[Shop | None]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Shop | None:
        pass

    @abstractmethod
    def filter_by_title(self, title: str) -> QuerySet[Shop | None]:
        pass

    @abstractmethod
    def create_shop(self, data: dict) -> Shop:
        pass

    @abstractmethod
    def update_shop(self, id: int, data: dict) -> None:
        pass

    @abstractmethod
    def delete_shop(self, id: int) -> None:
        pass
