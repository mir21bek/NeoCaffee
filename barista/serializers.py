from rest_framework import serializers

from administrator.models import Ingredients
from menu.models import Menu
from order.models import Order, OrderItem
from customers.models import BaseUser
from django.contrib.auth import get_user_model

from order.serializers import OrderMenuHistorySerializer, OrderExtraProductSerializer

User = get_user_model()


class BaristaAllMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ("product", "unit")


class BaristaMenuDetailSerializer(serializers.ModelSerializer):
    unit = BaristaAllMenuSerializer(many=True)

    class Meta:
        model = Menu
        fields = ("name", "description", "unit")


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "menu_quantity", "menu")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "role"]


class BaristaOrderSerializers(serializers.ModelSerializer):
    order_type = serializers.ChoiceField(choices=Order.TYPE_CHOICES)
    status = serializers.ChoiceField(choices=Order.STATUS_CHOICES)
    user_details = UserSerializer(source="user", read_only=True)
    items = MenuItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "order_type",
            "status",
            "user_details",
            "items",
            "created",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = instance.user

        if instance.order_type == "inplace" and user.position == "waiter":
            representation["user_details"] = {
                "username": user.first_name,
                "position": "Официант",
            }
        elif instance.order_type == "takeaway" and user.role == "client":
            representation["user_details"] = {
                "username": user.first_name,
                "role": "Клиент",
            }
        elif instance.order_type == "takeaway" and user.position == "barista":
            representation["user_details"] = {
                "username": user.first_name,
                "position": "Бариста",
            }
        elif instance.order_type == "takeaway" and user.role == "admin":
            representation["user_details"] = {
                "username": user.first_name,
                "role": "Менеджер",
            }

        return representation


class OrderStatusUpdateSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(
        help_text="Укажите id заказа для обновления его статуса"
    )
    new_status = serializers.ChoiceField(
        choices=Order.STATUS_CHOICES, help_text="выберите статус для заказа"
    )


class BaristaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = (
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
        )

    def update(self, instance, validated_data):
        instance


class BaristaOrderItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    menu_detail = OrderMenuHistorySerializer(source="menu", read_only=True)
    extra_product_detail = OrderExtraProductSerializer(
        source="extra_product", read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "menu_detail",
            "menu_quantity",
            "extra_product_detail",
            "extra_product_quantity",
        ]


class BaristaOrderSerializer(serializers.ModelSerializer):
    items = BaristaOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "created",
            "total_price",
            "items",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        order = Order.objects.create(**validated_data)

        for item in items_data:
            OrderItem.objects.create(order=order, **item)
        return order
