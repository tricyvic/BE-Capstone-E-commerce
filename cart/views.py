from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Cart, CartItem
from products.models import Product

class AddToCartView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))
        user = request.user

        product = Product.objects.filter(id=product_id).first()
        if not product:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        cart, _ = Cart.objects.get_or_create(user=user)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()

        return Response({"message": "Item added to cart."}, status=status.HTTP_200_OK)


class RemoveFromCartView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
            item = cart.items.get(product_id=product_id)
            item.delete()
            return Response({"message": "Item removed."}, status=status.HTTP_204_NO_CONTENT)
        except (Cart.DoesNotExist, CartItem.DoesNotExist):
            return Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)


class CartDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        items = [
            {
                "product": item.product.name,
                "quantity": item.quantity,
                "subtotal": item.subtotal(),
            }
            for item in cart.items.all()
        ]
        return Response({"cart_items": items, "total": cart.total_price()})
