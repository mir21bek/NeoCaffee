from rest_framework import serializers
from customers.models import BaseUser
from menu.models import Menu, Category
from branches.models import Branches


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
            "first_name",
            "last_name",
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


"""
Сериалайзер для категории меню
"""


class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "image")


"""
Сериалайзеры для меню
"""


class MenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["name", "description", "category", "image", "price"]


"""
Сериалайзеры для филиалов
"""


class AdminBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = (
            "id",
            "name",
            "image",
            "address",
            "phone_number",
            "map_link",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
            "SHIFT_CHOICES",
        )


"""
Сериалайзеры для сотрудников
"""


class AdminStaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = (
            "id",
            "login",
            "password",
            "first_name",
            "position",
            "date_of_birth",
            "phone_number",
            "branch",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
            "role",
            "SHIFT_CHOICES",
        )
        read_only_fields = ("role",)
