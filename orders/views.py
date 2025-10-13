from rest_framework import status, permissions, generics
from rest_framework.response import Response
from cart.models import Cart, CartItem
from .models import Order, OrderItem

class CheckoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

        if not cart.items.exists():
            return Response({"error": "Your cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        # Create an Order
        order = Order.objects.create(user=user)

        # Move items from cart to order
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )

        # Calculate total
        order.calculate_total()

        # Clear cart after checkout
        cart.items.all().delete()

        return Response(
            {"message": "Order placed successfully!", "order_id": order.id, "total": order.total_price},
            status=status.HTTP_201_CREATED,
        )
