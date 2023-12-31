from rest_framework import serializers
from customers.models import BaseUser
from menu.models import Menu, Category
from branches.models import Branches
from .models import Ingredients


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
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BaseUser
        fields = (
            "id",
            "login",
            "password",
            "phone_number",
            "date_of_birth",
            "first_name",
            "last_name",
            "position",
            "branch",
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


class MenuIngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = ("product", "quantity_used", "unit")


class MenuCreateSerializer(serializers.ModelSerializer):
    menu_ingredients = MenuIngredientsSerializer(many=True)

    class Meta:
        model = Menu
        fields = (
            "name",
            "description",
            "category",
            "image",
            "menu_ingredients",
            "price",
        )

    def create(self, validated_data):
        ingredients_data = validated_data.pop("menu_ingredients")
        menu = Menu.objects.create(**validated_data)

        for ingredient_data in ingredients_data:
            Ingredients.objects.create(menu_item=menu, **ingredient_data)

        return menu


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
            "last_name",
            "position",
            "date_of_birth",
            "phone_number",
            "branch",
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
            "role",
        )
        read_only_fields = ("role",)
