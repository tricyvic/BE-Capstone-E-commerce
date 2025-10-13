from django.urls import path
from .views import AddToCartView, RemoveFromCartView, CartDetailView

urlpatterns = [
    path("add/", AddToCartView.as_view(), name="add-to-cart"),
    path("remove/", RemoveFromCartView.as_view(), name="remove-from-cart"),
    path("", CartDetailView.as_view(), name="cart-detail"),
]
