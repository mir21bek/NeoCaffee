from rest_framework import serializers

from customers.models import BaseUser


class AdminLoginSerializer(serializers.ModelSerializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = BaseUser
        fields = ["login", "password"]


class WaiterLoginSerializer(serializers.ModelSerializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = BaseUser
        fields = ["login", "password"]


class WaiterCheckOTPSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField()

    class Meta:
        model = BaseUser
        fields = ["otp"]


class BaristaLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = BaseUser
        fields = ["phone_number"]


class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = (
            "login",
            "password",
            "phone_number",
            "date_of_birth",
            "username",
            "position",
            "branch",
            "monday",
            "monday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        )
