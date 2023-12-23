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

    serializer_class = CategorySerializer
    permission_classes = [IsClientUser]

    def get_queryset(self):
        queryset = Category.objects.all()
        branch_id = self.kwargs.get("branch_id")

        if branch_id:
            queryset = queryset.filter(branch_id=branch_id)
        return queryset


class MenuApiView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsClientUser]

    def get_queryset(self):
        queryset = Menu.objects.select_related("category", "branch").prefetch_related("extra_product")
        branch_id = self.kwargs.get("branch_id")

        if branch_id:
            queryset = queryset.filter(branch_id=branch_id)
            return queryset


class MenuListApiView(generics.ListAPIView):
    """Представление для получения списка доступных блюд.

    Это представление позволяет только чтение (GET) и требует аутентификации пользователя.
    """

    serializer_class = MenuSerializer
    permission_classes = [IsClientUser]

    def get_queryset(self):
        queryset = Menu.objects.select_related("category", "branch").prefetch_related("extra_product")
        category_slug = self.kwargs.get("category_slug")
        branch_id = self.kwargs.get("branch_id")

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        if branch_id:
            queryset = queryset.filter(branch_id=branch_id)
        return queryset


class PopularDishesView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsClientUser]

    def get_queryset(self):
        branch_id = self.kwargs.get("branch_id")

        if branch_id:
            today = timezone.now()
            first_day_of_month = today.replace(day=1)

            return (
                Menu.objects.filter(
                    branch_id=branch_id,
                    available=True,
                    order_items__order__created__gte=first_day_of_month,
                    order_items__order__created__lte=today,
                )
                .annotate(total_ordered=Count("order_items"))
                .order_by("-total_ordered")[:3]
            )
        return Menu.objects.none()
