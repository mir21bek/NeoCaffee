from rest_framework import serializers

from .models import Branches, CoffeeShop


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ("name", "address", "phone_number", "work_schedule", "image")


class CoffeeShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeShop
        fields = ("branch", "category", "menu")
