from django import forms


class ImageWithPreviewField(forms.ImageField):
    template_name = 'core/forms/widgets/image_with_preview.html'
