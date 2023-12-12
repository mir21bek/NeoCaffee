from rest_framework import serializers
from .models import AdminUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class AdminLoginSerializer(serializers.ModelSerializer):
    login = serializers.CharField(required=True, max_length=255)
    password = serializers.CharField(
        max_length=15, min_length=8, required=True, write_only=True
    )
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = AdminUser
        fields = ["login", "password", "tokens"]

    def validate(self, attrs):
        login = attrs.get("login", "")
        password = attrs.get("password", "")

        user = auth.authenticate(login=login, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credential, try again")
        if not user.is_active:
            raise AuthenticationFailed("Account disabled, contact admin")

        return {"login": user.login, "tokens": user.tokens()}


#
#
# class WaiterLoginSerializer(serializers.ModelSerializer):
#     login = serializers.CharField(required=True)
#     password = serializers.CharField(required=True, write_only=True)
#
#     class Meta:
#         model = WaiterUser
#         fields = ["login", "password"]
#
#
# class WaiterCheckOTPSerializer(serializers.ModelSerializer):
#     otp = serializers.IntegerField()
#
#     class Meta:
#         model = WaiterUser
#         fields = ["otp"]
#
#
# class BaristaLoginSerializer(serializers.ModelSerializer):
#     phone_number = serializers.CharField(required=True)
#
#     class Meta:
#         model = BaristaUser
#         fields = ["phone_number"]
