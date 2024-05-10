from typing import override

from django.db.models import QuerySet

from ..interfaces.shop_interfaces import IShopRepository
from ..models import Shop


class ShopRepository(IShopRepository):
    @override
    def get_all(self) -> QuerySet[Shop | None]:
        """Get all shops."""
        return Shop.objects.all()

    @override
    def get_by_id(self, id: int) -> Shop | None:
        """Get shop by id."""
        return Shop.objects.filter(pk=id).first()

    @override
    def search_by_title(self, title: str) -> QuerySet[Shop | None]:
        """Search shops by title."""
        return Shop.objects.filter(search_vector=title)

    @override
    def create_shop(self, data: dict) -> Shop:
        """Create a new shop."""
        return Shop.objects.create(**data)

    @override
    def update_shop(self, id: int, data: dict) -> None:
        """Update shop by id."""
        Shop.objects.filter(pk=id).update(**data)

    @override
    def delete_shop(self, id: int) -> None:
        """Delete shop by id."""
        Shop.objects.filter(pk=id).delete()
