from django.urls import path
from .views import CartListView, AddToCartView, RemoveFromCartView

urlpatterns = [
    path('', CartListView.as_view(), name='cart'),
    path('add/', AddToCartView.as_view(), name='add-to-cart'),
    path('remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]
