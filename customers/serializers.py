# serializers.py

from rest_framework import serializers
from order.serializers import OrderSerializer
from .models import BaseUser


from django.contrib.auth.hashers import make_password


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ["full_name", "phone_number", "date_of_birth"]
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


class CustomerProfileSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True, source="user.customer_orders")

    class Meta:
        model = BaseUser
        fields = ["full_name", "phone_number", "date_of_birth", "bonuses", "orders"]
        read_only_fields = ["bonuses"]

    def update(self, instance, validated_data):
        if instance.role == "client":
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
        return instance
