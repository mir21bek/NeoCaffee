from rest_framework import serializers

from menu.models import Menu, ExtraItem
from .models import Order, OrderItem
from branches.models import Branches


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ("image", "name")


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("image", "name", "price")


class ExtraItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraItem
        fields = ("name", "price")


class OrderItemSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)
    extra_product = ExtraItemSerializer(read_only=True)
    cashback = serializers.SerializerMethodField()

    def get_cashback(self, obj):
        return obj.apply_cashback()

    class Meta:
        model = OrderItem
        fields = (
            "order",
            "menu",
            "menu_quantity",
            "extra_product",
            "extra_product_quantity",
            "bonuses_used",
            "cashback",
        )


class OrderSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "user",
            "branch",
            "items",
            "created",
            "get_total_cost",
        ]
