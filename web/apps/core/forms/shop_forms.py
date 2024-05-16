from django import forms

from ..fields import DescriptionTextareaWidget, ImageUrlPreviewWidget, TitleInputWidget
from ..models import Shop


class CreateShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'description', 'imageUrl']
        widgets = {
            'title': TitleInputWidget(),
            'description': DescriptionTextareaWidget(),
            'imageUrl': ImageUrlPreviewWidget()
        }
