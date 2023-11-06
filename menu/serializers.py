from rest_framework import serializers

from .models import Category, Menu, ExtraItem, ExtraProduct


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category.

    Преобразует объекты Category в JSON и обратно.
    """

    class Meta:
        model = Category
        fields = ('name', 'image')  # Поля модели Category, включаемые в сериализацию

    def create(self, validated_data):
        """Создает новый объект Category."""
        category = Category.objects.create(**validated_data)
        return category

    def update(self, instance, validated_data):
        """Обновляет существующий объект Category."""
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()


class MenuSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Menu.

    Преобразует объекты Menu в JSON и обратно.
    """

    class Meta:
        model = Menu
        fields = ('name', 'category', 'description', 'image', 'price', 'available', 'popular')
        # Поля модели Menu, включаемые в сериализацию

    def create(self, validated_data):
        """Создает новый объект Menu."""
        menu = Menu.objects.create(**validated_data)
        return menu

    def update(self, instance, validated_data):
        """Обновляет существующий объект Menu."""
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.available = validated_data.get('available', instance.available)
        instance.popular = validated_data.get('popular', instance.popular)
        instance.save()


class ExtraItemSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ExtraItem."""

    class Meta:
        model = ExtraItem
        fields = ('name', 'price')

    def create(self, validated_data):
        """Создает новый объект ExtraItem."""
        extra_item = ExtraItem.objects.create(**validated_data)
        return extra_item

    def update(self, instance, validated_data):
        """Обновляет существующий объект ExtraItem."""
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()


class ExtraProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraProduct
        fields = ('menu', 'extra')