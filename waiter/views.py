from rest_framework import generics
from menu.models import Category, Menu
from administrator.permissions import IsWaiter
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from waiter.models import Table
from order.models import Order
from .serializers import (
    WaiterProfileSerializer,
    WaiterCategorySerializer,
    WaiterMenuSerializer,
    TableSerializer,
    WaiterOrderSerializer,
    WaiterOrderListSerializer
)


class WaiterProfileView(generics.RetrieveAPIView):
    serializer_class = WaiterProfileSerializer
    permission_classes = [IsWaiter]

    def get_object(self):
        return self.request.user


class WaiterCategoriesView(generics.ListAPIView):
    serializer_class = WaiterCategorySerializer
    permission_classes = [IsWaiter]

    def get_queryset(self):
        waiter = self.request.user
        return Category.objects.filter(branch=waiter.branch)


class WaiterMenuView(generics.ListAPIView):
    serializer_class = WaiterMenuSerializer
    permission_classes = [IsWaiter]

    def get_queryset(self):
        waiter = self.request.user
        category_slug = self.kwargs.get("category_slug")

        if category_slug:
            category = get_object_or_404(
                Category, slug=category_slug, branch=waiter.branch
            )
        else:
            raise NotFound("Не предоставлен slug категории.")
        return Menu.objects.filter(
            branch=waiter.branch, category=category, available=True
        )


class TableListView(generics.ListAPIView):
    serializer_class = TableSerializer
    permission_classes = [IsWaiter]
    queryset = Table.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = WaiterOrderSerializer
    permission_classes = [IsWaiter]

    def perform_create(self, serializer):
        serializer.save(
            order_type='inplace',
            branch=self.request.user.branch if hasattr(self.request.user, 'branch') else None,
            waiter=self.request.user if hasattr(self.request.user, 'id') else None
        )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = WaiterOrderListSerializer
