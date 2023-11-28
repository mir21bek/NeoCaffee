# serializers.py

from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.account.models import EmailAddress
from .models import BaseUser, WaiterUser, StaffUserProfile


class RegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = BaseUser
        fields = ["full_name", "phone_number", "date_of_birth"]

    def save(self):
        phone_number = self.validated_data["phone_number"]
        user = BaseUser(
            full_name=self.validated_data["full_name"],
            phone_number=phone_number,
            date_of_birth=self.validated_data["date_of_birth"],
        )
        user.save()
        return user


class CustomerLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = BaseUser
        fields = ["phone_number"]


class CheckOPTSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField()

    class Meta:
        model = BaseUser
        fields = ["otp"]
