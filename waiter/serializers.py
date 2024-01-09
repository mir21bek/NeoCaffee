from rest_framework import serializers
from menu.models import Category, Menu, ExtraItem
from customers.models import BaseUser
from waiter.models import Table
from order.models import Order, OrderItem


class WaiterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "date_of_birth",
            "monday",
            "monday_start_time",
            "monday_end_time",
            "tuesday",
            "tuesday_start_time",
            "tuesday_end_time",
            "wednesday",
            "wednesday_start_time",
            "wednesday_end_time",
            "thursday",
            "thursday_start_time",
            "thursday_end_time",
            "friday",
            "friday_start_time",
            "friday_end_time",
            "saturday",
            "saturday_start_time",
            "saturday_end_time",
            "sunday",
            "sunday_start_time",
            "sunday_end_time",
        ]


class WaiterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug")


class WaiterExtraItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraItem
        fields = ("id", "type_extra_product", "name", "price")


class WaiterMenuSerializer(serializers.ModelSerializer):
    extra_product = WaiterExtraItemSerializer(many=True)

    class Meta:
        model = Menu
        fields = ("id", "name", "price", "extra_product")


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ("id", "number", "status")


"""
Сериалайзеры для заказа
"""


class WaiterOrderMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["name", "price"]


class WaiterOrderExtraProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraItem
        fields = ["name", "price"]


class WaiterMTOSerializer(serializers.ModelSerializer):
    menu_detail = WaiterOrderMenuSerializer(source="menu", read_only=True)
    extra_product_detail = WaiterOrderExtraProductSerializer(
        source="extra_product", read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "menu_detail",
            "menu",
            "menu_quantity",
            "extra_product_detail",
            "extra_product",
            "extra_product_quantity",
        ]


class WaiterOrderSerializer(serializers.ModelSerializer):
    items = WaiterMTOSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "items",
            "branch",
            "table",
            "order_type",
            "created",
            "total_price",
            "waiter",
        ]
        write_only_fields = ['order_type', 'branch', 'waiter']


class WaiterOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "menu",
            "status"
            "table",
            "order_type",
            "created",
            "total_price",
            "waiter",
        ]