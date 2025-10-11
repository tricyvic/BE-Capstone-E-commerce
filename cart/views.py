from rest_framework import generics, permissions
from .models import CartItem
from .serializers import CartItemSerializer
from products.models import Product
from rest_framework.response import Response
from rest_framework import status

class CartListView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


class AddToCartView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartItemSerializer

    def post(self, request):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))
        product = Product.objects.get(id=product_id)

        cart_item, created = CartItem.objects.get_or_create(
            user=request.user, product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return Response({"message": "Added to cart"}, status=status.HTTP_200_OK)


class RemoveFromCartView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        CartItem.objects.filter(user=request.user, product_id=pk).delete()
        return Response({"message": "Removed from cart"}, status=status.HTTP_204_NO_CONTENT)
