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
    order_type = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    total_price = serializers.IntegerField(min_value=0, read_only=True)
    branch = serializers.CharField(read_only=True)
    bonuses_used = serializers.IntegerField(min_value=0, read_only=True)
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
        mto_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)

        for mto in mto_data:
            drop_id = validated_data.pop("id")
            OrderItem.objects.create(order=order, **mto)
            return order
