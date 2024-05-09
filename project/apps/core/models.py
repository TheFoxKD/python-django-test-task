from django.db import models


class Shop(models.Model):
    """
    Represents an online store.

    Attributes:
        id (int): The unique identifier of the store.
        title (str): The stores name.
        description (str): Description of the store.
        imageUrl (str): URL of the stores image.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    imageUrl = models.URLField()

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    Представляет продукт в интернет-магазине.

    Attributes:
        id (int): The unique identifier of the product.
        description (str): The description of the product.
        title (str): The name of the product.
        amount (int): The number of products in stock.
        price (float): The price of the product.
        active (bool): Whether the product is available for purchase.
        shop (Shop): The store in which the product is sold.
    """
    description = models.TextField()
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.FloatField()
    images = models.JSONField(default=list)
    active = models.BooleanField(default=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title


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
    title = models.CharField(max_length=255)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    products = models.ManyToManyField(Product, related_name='categories')

    def __str__(self):
        return self.title
