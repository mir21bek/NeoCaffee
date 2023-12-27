from rest_framework import serializers
from branches.models import Branches
from menu.models import Menu, ExtraItem
from .models import Order, OrderItem


class OrderMenuHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['image', 'name', 'description', 'price']


class OrderExtraProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraItem
        fields = ['name', 'price']


class MTOSerializer(serializers.ModelSerializer):
    menu_detail = OrderMenuHistorySerializer(source='menu', read_only=True)
    extra_product_detail = OrderExtraProductSerializer(source='extra_product', read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            "menu",
            "menu_detail",
            "menu_quantity",
            "extra_product",
            "extra_product_detail",
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
        return order


class OrderBranchInHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ('image', 'name')


class OrderHistorySerializer(serializers.ModelSerializer):
    branch = OrderBranchInHistorySerializer()
    items = MTOSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "branch",
            "created",
            "items",
        ]
