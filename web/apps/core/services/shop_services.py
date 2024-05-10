from dataclasses import dataclass

from django.db.models import QuerySet

from web.apps.core.interfaces.shop_interfaces import IShopRepository
from web.apps.core.models import Shop


@dataclass
class ShopService:
    """Service for managing shops."""
    shop_repository: IShopRepository

    def get_all_shops(self) -> QuerySet[Shop | None]:
        """Get all shops."""
        return self.shop_repository.get_all()

    def search_shops_by_title(self, title: str) -> QuerySet[Shop | None]:
        """Search shops by title."""
        return self.shop_repository.filter_by_title(title)

    def create_shop(self, data: dict) -> Shop:
        """Create a new shop."""
        return self.shop_repository.create_shop(data)

    def update_shop(self, id: int, data: dict) -> None:
        """Update shop by id."""
        return self.shop_repository.update_shop(id, data)

    def delete_shop(self, id: int) -> None:
        """Delete shop by id."""
        return self.shop_repository.delete_shop(id)
