from rest_framework import serializers

from order.models import Order

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["full_name", "role"]


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
                "username": user.full_name,
                "role": "Официант",
            }
        elif instance.order_type == "takeaway" and user.role == "client":
            representation["user_details"] = {
                "username": user.full_name,
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
