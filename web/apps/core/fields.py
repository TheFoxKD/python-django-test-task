from django import forms


class ImageUrlPreviewWidget(forms.ClearableFileInput):
    template_name = 'core/forms/widgets/image_with_preview.html'


class ImageUrlPreviewField(forms.ImageField):
    widget = ImageUrlPreviewWidget
