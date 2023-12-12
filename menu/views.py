from rest_framework import generics, permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Menu, ExtraItem
from .serializers import (
    CategorySerializer,
    MenuSerializer,
    ExtraItemSerializer,
    MenuAndExtraItemsSerializer,
)
from .signals import post_category_save, post_menu_save


class CategoryApiView(generics.ListAPIView):
    """Представление для получения списка всех категорий.

    Это представление позволяет только чтение (GET) и требует аутентификации пользователя.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuListApiView(generics.ListAPIView):
    """Представление для получения списка доступных блюд.

    Это представление позволяет только чтение (GET) и требует аутентификации пользователя.
    """

    queryset = Menu.objects.all().filter(available=True)
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Menu.objects.filter(available=True)
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
            return queryset


class PopularDishesView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.filter(popular=True)[:5]


class MenuAndExtraItemsView(APIView):
    def get(self, request, format=None):
        menus = Menu.objects.filter(available=True)
        extra_items = ExtraItem.objects.all()

        serializer = MenuAndExtraItemsSerializer(
            {"menus": menus, "extra_items": extra_items}
        )

        return Response(serializer.data)
