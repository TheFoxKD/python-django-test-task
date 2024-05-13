from django import forms

from ..fields import ImageWithPreviewField
from ..models import Shop


class CreateShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'description', 'image']

    image = ImageWithPreviewField()
