from django.db.models import Count
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from administrator.permissions import IsClientUser
from branches.models import Branches
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
    queryset = Category.objects.all()


class MenuApiView(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsClientUser]
    queryset = Menu.objects.select_related("category").prefetch_related("extra_product")


class MenuListApiView(generics.ListAPIView):
    """Представление для получения списка доступных блюд.

    Это представление позволяет только чтение (GET) и требует аутентификации пользователя.
    """

    serializer_class = MenuSerializer
    permission_classes = [IsClientUser]

    def get_queryset(self):
        queryset = Menu.objects.select_related("category").prefetch_related(
            "extra_product"
        )
        category_slug = self.kwargs.get("category_slug")

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset


class MenuDetailAPIView(generics.RetrieveAPIView):
    queryset = Menu.objects.select_related("category")
    serializer_class = MenuSerializer
    permission_classes = [IsClientUser]
    lookup_field = "id"


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
