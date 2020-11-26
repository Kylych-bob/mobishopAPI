from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product


User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Product


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')