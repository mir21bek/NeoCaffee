# serializers.py

from rest_framework import serializers
from order.serializers import OrderSerializer, OrderHistorySerializer
from .models import BaseUser


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ["first_name", "phone_number", "date_of_birth"]
        extra_kwargs = {
            "password": {"write_only": True},
            "date_of_birth": {"format": "%d %m %Y"},
        }

    def create(self, validated_data):
        validated_data["role"] = "client"
        return BaseUser.objects.create(**validated_data)


class CustomerLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = BaseUser
        fields = ["phone_number"]


class CustomerCheckOTPSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField()

    class Meta:
        model = BaseUser
        fields = ["otp"]


class OrderItemSerializer(serializers.Serializer):
    order = serializers.IntegerField()
    menu = serializers.DictField()
    menu_quantity = serializers.IntegerField()
    extra_product = serializers.CharField(allow_null=True)
    extra_product_quantity = serializers.IntegerField()
    bonuses_used = serializers.CharField()
    cashback = serializers.FloatField()


class ProfileOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField()
    user = serializers.IntegerField()
    branch = serializers.DictField()
    items = OrderItemSerializer(many=True)
    created = serializers.DateTimeField()
    get_total_cost = serializers.FloatField()


class CustomerProfileSerializer(serializers.ModelSerializer):
    active_orders = serializers.SerializerMethodField()
    completed_orders = serializers.SerializerMethodField()

    class Meta:
        model = BaseUser
        fields = (
            "first_name",
            "phone_number",
            "date_of_birth",
            "bonuses",
            "active_orders",
            "completed_orders",
        )
        read_only_fields = ["bonuses"]

    def get_active_orders(self, obj):
        active_statuses = ["new", "in_process"]
        orders = obj.customer_orders.filter(status__in=active_statuses)
        return OrderHistorySerializer(orders, many=True).data

    def get_completed_orders(self, obj):
        completed_statuses = ["done", "completed"]
        orders = obj.customer_orders.filter(status__in=completed_statuses)
        return OrderHistorySerializer(orders, many=True).data

    def update(self, instance, validated_data):
        if instance.role == "client":
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
        return instance
