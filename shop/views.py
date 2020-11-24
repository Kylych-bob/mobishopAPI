from rest_framework import generics
from .models import Products, Category, Orders
from .serializers import ProductSerializer
# Create your views here.

class ProductsApiView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


