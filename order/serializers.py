from rest_framework import serializers

from .models import Order, OrderItem
from menu.models import ExtraItem


class OrderExtraItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraItem
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    extra_product = OrderExtraItemSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'menu', 'extra_product', 'price', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'items', 'created', 'updated', 'paid')
