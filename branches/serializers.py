from rest_framework import serializers

from .models import Branches, CoffeeShop


class CoffeeShopSerializer(serializers.ModelSerializer):
    branch = serializers.StringRelatedField()
    category = serializers.StringRelatedField(many=True)
    menu = serializers.StringRelatedField(many=True)

    class Meta:
        model = CoffeeShop
        fields = ("branch", "category", "menu")


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = (
            "id",
            "name",
            "address",
            "map_link",
            "phone_number",
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
            "image",
        )
