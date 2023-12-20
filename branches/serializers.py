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
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
            "image",
        )
