from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, Shop

admin.site.register(Product)
admin.site.register(Category)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'display_image')
    search_fields = ('title',)
    readonly_fields = ('id',)

    def display_image(self, obj):
        print(obj.imageUrl.url)
        return format_html('<img src="{}" width="100" />'.format(obj.imageUrl.url))

    display_image.short_description = 'Image'

    def save_model(self, request, obj, form, change):
        if 'imageUrl' in request.FILES:
            obj.imageUrl = request.build_absolute_uri(obj.imageUrl.url)
        super().save_model(request, obj, form, change)
