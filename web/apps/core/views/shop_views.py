from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from ..models import Shop
from ..repositories.shop_repositories import ShopRepository
from ..services.shop_services import ShopService

# Dependency Injection of ShopService 🤣😆
shop_service = ShopService(ShopRepository())


class ShopListView(ListView):
    model = Shop
    template_name = 'core/shop/shop_list.html'

    def get_queryset(self):
        if 'search' in self.request.GET:
            return shop_service.search_shops_by_title(self.request.GET['search'])

        return shop_service.get_all_shops()


class ShopSearchView(ListView):
    pass


class ShopDetailView(View):
    pass


class ShopUpdateView(UpdateView):
    pass


class ShopCreateView(CreateView):
    pass
