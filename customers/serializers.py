# serializers.py

from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.account.models import EmailAddress
from .models import BaseUser, WaiterUser, BaristaUser, StaffUserProfile


class BaseUserUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser  # Замените на нужную модель (WaiterUser, BaristaUser, ...)
        fields = [
            "id",
            "full_name",
            "phone_number",
            "otp",
            "date_of_birth",
            "is_active",
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    user = BaseUserUserSerializer()

    class Meta:
        model = StaffUserProfile
        fields = [
            "id",
            "user",
            "role",
            "login",
            "full_name",
            "phone_number",
            "date_of_birth",
            "schedule",
            "is_active",
        ]


class PhoneNumberVerificationSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class PhoneNumberVerificationCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=17)
    otp = serializers.CharField(max_length=4)
    date_of_birth = serializers.DateField()

    def create(self, validated_data):
        # Создаем пользователя через allauth
        user = get_adapter().create_user(self.context["request"], validated_data)
        setup_user_email(self.context["request"], user, [])
        EmailAddress.objects.create(
            user=user, email=user.phone_number, primary=True, verified=True
        )
        return user


class WaiterBaristaRegisterSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=50)
    otp = serializers.CharField(max_length=4)

    def create(self, validated_data):
        # Создайте WaiterUser или BaristaUser в зависимости от вашего выбора
        user = get_adapter().create_user(self.context["request"], validated_data)
        return user
