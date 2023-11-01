from rest_framework import serializers

from .models import Category, Menu


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category.

    Этот сериализатор используется для преобразования объектов Category в JSON и наоборот.
    """

    class Meta:
        model = Category
        fields = ['name']  # Поля модели Category, которые будут включены в сериализацию

    def create(self, validated_data):
        """Метод для создания нового объекта Category.

        Args:
            validated_data (dict): Валидированные данные для создания объекта Category.

        Returns:
            Category: Созданный объект Category.
        """
        category = Category.objects.create(**validated_data)
        return category

    def update(self, instance, validated_data):
        """Метод для обновления существующего объекта Category.

        Args:
            instance (Category): Существующий объект Category, который нужно обновить.
            validated_data (dict): Валидированные данные для обновления объекта Category.

        Returns:
            Category: Обновленный объект Category.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class MenuSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Menu.

    Этот сериализатор используется для преобразования объектов Menu в JSON и наоборот.
    """

    class Meta:
        model = Menu
        fields = ('name', 'category', 'description', 'image', 'price', 'available', 'popular')
        # Поля модели Menu, которые будут включены в сериализацию

    def create(self, validated_data):
        """Метод для создания нового объекта Menu.

        Args:
            validated_data (dict): Валидированные данные для создания объекта Menu.

        Returns:
            Menu: Созданный объект Menu.
        """
        menu = Menu.objects.create(**validated_data)
        return menu
