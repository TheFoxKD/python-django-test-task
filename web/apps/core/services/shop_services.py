from dataclasses import dataclass

from django.db.models import QuerySet

from ..interfaces.shop_interfaces import IShopRepository
from ..models import Shop
from ..types import URL


@dataclass
class ShopService:
    """Service for managing shops."""
    shop_repository: IShopRepository

    def get_all_shops(self) -> QuerySet[Shop | None]:
        """Get all shops."""
        return self.shop_repository.get_all()

    def search_shops_by_title(self, title: str) -> QuerySet[Shop | None]:
        """Search shops by title."""
        return self.shop_repository.search_by_title(title)

    def create_shop(self, title: str, description: str, image_url: URL) -> Shop:
        """Create a new shop."""
        return self.shop_repository.create_shop(title, description, image_url)

    def update_shop(self, id: int, data: dict) -> None:
        """Update shop by id."""
        return self.shop_repository.update_shop(id, data)

    def delete_shop(self, id: int) -> None:
        """Delete shop by id."""
        return self.shop_repository.delete_shop(id)
