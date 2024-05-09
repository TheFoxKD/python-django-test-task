from django.contrib import admin

from web.apps.core.models import Category, Product, Shop

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Category)
