from django import forms

from ..models import Shop


class CreateShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'description']
