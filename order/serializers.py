from rest_framework import serializers

from menu.models import Menu, ExtraItem
from .models import Order, OrderItem
from branches.models import Branches


class MTOSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "menu",
            "menu_quantity",
            "extra_product",
            "extra_product_quantity",
        ]


class OrderSerializer(serializers.ModelSerializer):
    cashback = serializers.SerializerMethodField()
    items = MTOSerializer(many=True)

    def get_cashback(self, obj):
        return obj.apply_cashback()

    class Meta:
        model = Order
        fields = [
            "id",
            "order_type",
            "status",
            "branch",
            "user",
            "bonuses_used",
            "created",
            "total_price",
            "cashback",
            "items",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        order = Order.objects.create(**validated_data)

        for item in items_data:
            OrderItem.objects.create(order=order, **item)
        order.save()
        return order
