from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    """
    Represents an online store.

    Attributes:
        id (int): The unique identifier of the store.
        title (str): The stores name.
        description (str): Description of the store.
        imageUrl (str): URL of the stores image.
        search_vector (SearchVectorField): The search vector for the store.
    """
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    imageUrl = models.URLField(verbose_name=_('Image URL'))
    # Search vector for full-text search in the title and description fields.
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [GinIndex(fields=['search_vector'])]
        verbose_name = _('Shop')
        verbose_name_plural = _('Shops')

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'<Shop id={self.pk}, title={self.title}>'

    def get_absolute_url(self):
        return reverse('core:shops:detail', kwargs={'pk': self.pk})


class Product(models.Model):
    """
    Represents a product in an online store.

    Attributes:
        id (int): The unique identifier of the product.
        description (str): The description of the product.
        title (str): The name of the product.
        amount (int): The number of products in stock.
        price (float): The price of the product.
        active (bool): Whether the product is available for purchase.
        shop (Shop): The store in which the product is sold.
    """
    description = models.TextField(verbose_name=_('Description'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    amount = models.IntegerField(verbose_name=_('Amount'))
    price = models.FloatField(verbose_name=_('Price'))
    images = models.JSONField(default=list, verbose_name=_('Images'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products', verbose_name=_('Shop'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'<Product id={self.pk}, title={self.title}>'


class Category(models.Model):
    """
    Represents a category of products in an online store.

    Attributes:
        id (int): The unique identifier of the category.
        title (str): The name of the category.
        description (str): Description of the category.
        parent (Category): The parent category of the category.
        products (list[Product]): The products in the category.
    """
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children',
                               verbose_name=_('Parent category'))
    products = models.ManyToManyField(Product, related_name='categories', verbose_name=_('Products'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'<Category id={self.pk}, title={self.title}>'
