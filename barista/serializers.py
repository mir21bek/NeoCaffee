from rest_framework import serializers

from order.models import Order
from customers.models import BaseUser

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "role"]


class BaristaOrderSerializers(serializers.ModelSerializer):
    user_details = UserSerializer(source="user", read_only=True)

    class Meta:
        model = Order
        fields = (
            "order_type",
            "status",
            "custom_order_id",
            "user_details",
            "menu",
            "created",
            "updated",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = instance.user

        if instance.order_type == "inplace" and user.role == "waiter":
            representation["user_details"] = {
                "username": user.first_name,
                "role": "Официант",
            }
        elif instance.order_type == "takeaway" and user.role == "client":
            representation["user_details"] = {
                "username": user.first_name,
                "role": "Клиент",
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
