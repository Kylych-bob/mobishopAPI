from django.urls import path

from .views import ProductsApiView

urlpatterns = [
    path('', ProductsApiView.as_view()),
]