from rest_framework import generics, permissions
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Product, Category
from .serializers import ProductSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


User = get_user_model()


class ProductListApiView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


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