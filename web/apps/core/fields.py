from django import forms


class ImageUrlPreviewWidget(forms.ClearableFileInput):
    template_name = 'core/forms/widgets/image_with_preview.html'


class ImageUrlPreviewField(forms.ImageField):
    widget = ImageUrlPreviewWidget


class TitleInputWidget(forms.TextInput):
    template_name = 'core/forms/widgets/title_input.html'


class DescriptionTextareaWidget(forms.Textarea):
    template_name = 'core/forms/widgets/description_textarea.html'
