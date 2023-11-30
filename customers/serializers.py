# serializers.py

from rest_framework import serializers
from .models import BaristaUser, CustomerUser, WaiterUser


class RegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = CustomerUser
        fields = ["username", "phone_number", "date_of_birth"]

    def save(self):
        phone_number = self.validated_data["phone_number"]
        user = CustomerUser(
            username=self.validated_data["username"],
            phone_number=phone_number,
            date_of_birth=self.validated_data["date_of_birth"],
        )
        user.save()
        return user


class CustomerLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = CustomerUser
        fields = ["phone_number"]


class CustomerCheckOTPSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField()

    class Meta:
        model = CustomerUser
        fields = ["otp"]


class WaiterLoginSerializer(serializers.ModelSerializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = WaiterUser
        fields = ["login", "password"]


class WaiterCheckOTPSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField()

    class Meta:
        model = WaiterUser
        fields = ["otp"]


class BaristaLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = BaristaUser
        fields = ["phone_number"]
