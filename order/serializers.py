from rest_framework import serializers

from menu.models import Menu, ExtraItem
from .models import Order, OrderItem
from menu.serializers import ExtraItemSerializer, MenuSerializer


class OrderMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["name", "price"]


class OrderExtraProduct(serializers.ModelSerializer):
    class Meta:
        model = ExtraItem
        fields = ["name", "price"]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["menu_quantity", "extra_product_quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    menu = OrderMenuSerializer(many=True)
    extra_products = OrderExtraProduct(many=True)
    cashback = serializers.SerializerMethodField()

    def get_cashback(self, obj):
        return obj.get_cashback()

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "user",
            "menu",
            "extra_products",
            "items",
            "bonuses_writen_off",
            "cashback",
            "created",
            "updated",
            "branch",
            "get_total_cost",
        ]

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.apply_bonuses(
            validated_data.get("bonuses_writen_off", instance.bonuses_writen_off)
        )
        return instance
