from django import forms

from ..fields import DescriptionTextareaWidget, ImagePreviewWidget, ImageUrlPreviewField, TitleInputWidget
from ..models import Shop
from ..repositories.shop_repositories import ShopRepository
from ..services.shop_services import ShopService
from ..types import URL

shop_service = ShopService(ShopRepository())


class CreateShopForm(forms.ModelForm):
    image = ImageUrlPreviewField(required=False)

    class Meta:
        model = Shop
        fields = ['title', 'description', 'image']
        widgets = {
            'title': TitleInputWidget(),
            'description': DescriptionTextareaWidget(),
            'image': ImagePreviewWidget()
        }

    def create_shop(self):
        title: str = self.cleaned_data.get('title')
        description: str = self.cleaned_data.get('description')
        image_url: URL = self.cleaned_data.get('image')

        shop = shop_service.create_shop(
            title=title,
            description=description,
            image_url=image_url
        )

        return shop
