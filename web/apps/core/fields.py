from django import forms

from .services.image_services import ImageService

image_service = ImageService


class ImagePreviewWidget(forms.ClearableFileInput):
    template_name = 'core/forms/widgets/image_with_preview.html'


class ImageUrlPreviewField(forms.ImageField):
    widget = ImagePreviewWidget

    def clean(self, data, initial=None):
        image_file = super().clean(data, initial)

        if image_file:
            image_url = image_service.save_image_and_return_url(image_file=image_file)
            return image_url

        raise forms.ValidationError('Invalid file')


class TitleInputWidget(forms.TextInput):
    template_name = 'core/forms/widgets/title_input.html'


class DescriptionTextareaWidget(forms.Textarea):
    template_name = 'core/forms/widgets/description_textarea.html'
