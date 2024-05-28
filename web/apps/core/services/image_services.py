from django.core.files import File
from django.core.files.storage import default_storage

from ..types import URL


class ImageService:
    @staticmethod
    def save_image_and_return_url(image_file: File) -> URL:
        file_name = default_storage.save(image_file.name, image_file)
        return default_storage.url(file_name)
