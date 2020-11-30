from datetime import timedelta
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework import generics, permissions
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category
from .serializers import ProductSerializer, CategoryApiSerializer, UserSerializer



User = get_user_model()


class ProductListApiView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    """  search  """
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'title', 'price',)


    # filter by price
    def get_queryset(self):
        price = self.request.query_params.get('price')
        queryset = super().get_queryset()
        if price:
            price_from, price_to = price.split('-')
            queryset = queryset.filter(
                price__gt=price_from, 
                price__lt=price_to
            )
        return queryset


class CategoryApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryApiSerializer



class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer








# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer