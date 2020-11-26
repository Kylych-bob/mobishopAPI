from django.db import models
from datetime import date
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        Category, verbose_name = 'Категория', on_delete=models.CASCADE,
        null=True, blank=True
    )
    title = models.CharField(max_length=155, verbose_name = 'Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = 'Цена')
    description = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    available = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.title



# class Orders(models.Model):
#     date = models.DateTimeField(auto_now_add=True)
#     price = models.FloatField(null=True, blank=True)
#     quantity = models.PositiveSmallIntegerField(default=0)

#     def __str__(self):
#         return f"{self.client_id} - {self.seller_id}"


