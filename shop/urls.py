from django.urls import path

from .views import ProductListApiView, ProductDetailApiView, CategoryApiView

urlpatterns = [
    path('products/', ProductListApiView.as_view()),
    path('products/<int:pk>/', ProductDetailApiView.as_view()),
    path('categories/', CategoryApiView.as_view()),
]