from rest_framework import serializers
from menu.models import Category, Menu
from customers.models import BaseUser


class WaiterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "date_of_birth",
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
        ]


class WaiterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class WaiterMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("id", "name", "price")
