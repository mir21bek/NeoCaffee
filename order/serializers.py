from rest_framework import serializers
from .models import Order, OrderItem
from menu.serializers import ExtraItemSerializer, MenuSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)
    extra_product = ExtraItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "branch",
            "menu",
            "menu_quantity",
            "extra_product",
            "extra_product_quantity",
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer()
    total_price = serializers.SerializerMethodField()
    cashback = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return obj.get_total_cost()

    def get_cashback(self, obj):
        return obj.get_cashback()

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "menu",
            "extra_products",
            "paid",
            "status",
            "items",
            "total_price",
            "cashback",
            "created",
            "updated",
        )
