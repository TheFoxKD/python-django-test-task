from django.views.generic import CreateView, ListView, UpdateView

from web.apps.core.models import Shop
from web.apps.core.repositories.shop_repositories import ShopRepository
from web.apps.core.services.shop_services import ShopService

# Dependency Injection of ShopService 🤣😆
shop_service = ShopService(ShopRepository())


class ShopListView(ListView):
    model = Shop
    template_name = 'core/shop/shop_list.html'

    def get_queryset(self):
        return shop_service.get_all_shops()


class ShopSearchView(ListView):
    pass


class ShopUpdateView(UpdateView):
    pass


class ShopCreateView(CreateView):
    pass
