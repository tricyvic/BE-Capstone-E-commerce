from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Order, OrderItem
from cart.models import CartItem
from products.models import Product
from decimal import Decimal

class CheckoutView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items:
            return Response({"error": "Cart is empty"}, status=400)

        total = sum(item.product.price * item.quantity for item in cart_items)
        order = Order.objects.create(user=request.user, total_price=Decimal(total))

        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            item.delete()

        order.payment_status = "Paid"  # Mock payment success
        order.save()

        return Response({"message": "Order placed successfully", "order_id": order.id})
