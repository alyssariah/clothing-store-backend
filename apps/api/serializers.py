from rest_framework import serializers
from apps.api.models import Product, CartItem, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'pictureUrl', 'price', 'description', 'category',)

class CartItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = CartItem
        fields = ('id', 'owner', 'product', 'qty', 'size',)

class CartFullSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = CartItem
        fields = ('id', 'owner', 'product', 'qty', 'size',)
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Order
        fields = ('id', 'owner', 'items', 'created_at', 'ordered',)

class OrderFullSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    items = CartFullSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'owner', 'items', 'created_at', 'ordered',)

