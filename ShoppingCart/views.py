from django.shortcuts import render
from .models import Cart, CartItem
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from Products.models import Product
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    data = request.data
    product_id = data['product_id']
    quantity = data.get('quantity')

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)
    
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += quantity
    cart_item.save()

    return Response({'message': f'Added {quantity} {product.name} to the cart'}, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return Response({'error': 'Cart not found'}, status=404)

    cart_items = cart.items.all()
    items = []
    for item in cart_items:
        items.append({
            'product_id' : item.product.id,
            'product_name': item.product.name,
            'quantity': item.quantity,
            'price': item.product.price,
            'total_price': item.quantity * item.product.price
        })
    
    return Response({'cart_items': items}, status=200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request):
    data = request.data
    product_id = data['product_id']

    try:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
        cart_item.delete()

        return Response({'message': 'Product removed from cart'}, status=200)
    
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        return Response({'error': 'Product not found in cart'}, status=404)
