from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ("category", "image", )
        model = Products


