from django.db.models import QuerySet

from web.apps.core.models import Shop


class ShopRepository:
    @staticmethod
    def get_all() -> QuerySet[Shop | None]:
        return Shop.objects.all()

    @staticmethod
    def get_by_id(id: int) -> Shop | None:
        return Shop.objects.filter(pk=id).first()

    @staticmethod
    def filter_by_title(title: str) -> QuerySet[Shop | None]:
        return Shop.objects.filter(title__icontains=title)

    @staticmethod
    def create_shop(data: dict) -> Shop:
        return Shop.objects.create(**data)

    @staticmethod
    def update_shop(id: int, data: dict) -> None:
        Shop.objects.filter(pk=id).update(**data)

    @staticmethod
    def delete_shop(id: int) -> None:
        Shop.objects.filter(pk=id).delete()
