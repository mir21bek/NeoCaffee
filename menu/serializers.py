from rest_framework import serializers

from .models import Category, Menu, ExtraItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug", "image")


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            "id",
            "name",
            "slug",
            "category",
            "description",
            "image",
            "price",
            "available",
        )


class ExtraItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraItem
        fields = ("name", "price")


class MenuAndExtraItemsSerializer(serializers.Serializer):
    menus = MenuSerializer(many=True, read_only=True)
    extra_items = ExtraItemSerializer(many=True, read_only=True)
