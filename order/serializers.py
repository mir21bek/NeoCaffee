from rest_framework import serializers

from .models import Order, OrderItem
from menu.models import ExtraItem, Menu


class OrderExtraItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraItem
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('name', 'price')


class OrderItemSerializer(serializers.ModelSerializer):
    menu = MenuItemSerializer()
    extra_product = OrderExtraItemSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'menu', 'extra_product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'items', 'created', 'updated', 'paid')
