from rest_framework import serializers

from .models import Category, Menu, ExtraItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug", "image")


class ExtraItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraItem
        fields = ("type_extra_product", "name", "price")


class MenuSerializer(serializers.ModelSerializer):
    extra_product = ExtraItemSerializer(many=True)

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
            "extra_product",
        )
