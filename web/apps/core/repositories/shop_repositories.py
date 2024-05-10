from typing import override

from django.db.models import QuerySet

from web.apps.core.interfaces.shop_interfaces import IShopRepository
from web.apps.core.models import Shop


class ShopRepository(IShopRepository):
    @override
    def get_all(self) -> QuerySet[Shop | None]:
        return Shop.objects.all()

    @override
    def get_by_id(self, id: int) -> Shop | None:
        return Shop.objects.filter(pk=id).first()

    @override
    def filter_by_title(self, title: str) -> QuerySet[Shop | None]:
        return Shop.objects.filter(title__icontains=title)

    @override
    def create_shop(self, data: dict) -> Shop:
        return Shop.objects.create(**data)

    @override
    def update_shop(self, id: int, data: dict) -> None:
        Shop.objects.filter(pk=id).update(**data)

    @override
    def delete_shop(self, id: int) -> None:
        Shop.objects.filter(pk=id).delete()
