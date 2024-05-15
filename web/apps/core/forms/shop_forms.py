from django import forms

from ..fields import ImageUrlPreviewField
from ..models import Shop


class CreateShopForm(forms.ModelForm):
    image = ImageUrlPreviewField(required=False)

    class Meta:
        model = Shop
        fields = ['title', 'description', 'image']
