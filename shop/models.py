from django.db import models
from datetime import date


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_id = models.IntegerField()

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=155)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name


class Orders(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    # client_id = models.IntegerField()
    # seller_id = models.IntegerField()

    def __str__(self):
        return f"{self.client_id} - {self.seller_id}"