from django.db.models import Count
from django.utils import timezone
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from administrator.permissions import IsClientUser
from .models import Category, Menu
from .serializers import (
    CategorySerializer,
    MenuSerializer,
)


class CategoryApiView(generics.ListAPIView):
    """Представление для получения списка всех категорий.

    Это представление позволяет только чтение (GET) и требует аутентификации пользователя.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsClientUser]


class MenuListApiView(generics.ListAPIView):
    """Представление для получения списка доступных блюд.

    Это представление позволяет только чтение (GET) и требует аутентификации пользователя.
    """

    queryset = Menu.objects.all().filter(available=True)
    serializer_class = MenuSerializer
    permission_classes = [IsClientUser]

    def get_queryset(self):
        queryset = Menu.objects.filter(available=True)
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
            return queryset


class PopularDishesView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsClientUser]

    def get_queryset(self):
        today = timezone.now()
        first_day_of_month = today.replace(day=1)

        return (
            Menu.objects.filter(
                available=True,
                order_items__order__created__gte=first_day_of_month,
                order_items__order__created__lte=today,
            )
            .annotate(total_ordered=Count("order_items"))
            .order_by("-total_ordered")[:3]
        )
