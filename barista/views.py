from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from administrator.permissions import IsBarista, IsAdminUser, IsWaiter
from menu.models import Menu
from menu.serializers import MenuSerializer
from order.models import Order
from drf_yasg.utils import swagger_auto_schema
from .serializers import (
    BaristaOrderSerializers,
    OrderStatusUpdateSerializer,
    BaristaProfileSerializer,
    BaristaOrderSerializer,
)


class OrdersView(APIView):
    permission_classes = [IsBarista | IsAdminUser]

    def get(self, request, *args, **kwargs):
        user_branch = request.user.branch
        order_status = request.query_params.get("status", None)
        order_type = request.query_params.get("type", None)

        orders = Order.objects.filter(branch=user_branch)
        if order_status:
            orders = orders.filter(order_status=order_status)
        if order_type:
            orders = orders.filter(order_type=order_type)
        orders = orders.order_by("-created")

        serializer = BaristaOrderSerializers(orders, many=True)
        return Response(serializer.data)


class UpdateStatusAPIView(APIView):
    permission_classes = [IsBarista | IsAdminUser | IsWaiter]

    @swagger_auto_schema(request_body=OrderStatusUpdateSerializer)
    def post(self, request, *args, **kwargs):
        serializer = OrderStatusUpdateSerializer(data=request.data)
        if serializer.is_valid():
            order_id = serializer.validated_data["order_id"]
            new_status = serializer.validated_data["new_status"]

            user_branch = request.user.branch
            try:
                order = Order.objects.get(id=order_id, branch=user_branch)
            except Order.DoesNotExist:
                return Response(
                    {"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND
                )

            if new_status == "in_process":
                order.set_in_process()
            elif new_status == "completed":
                order.set_completed()
            elif new_status == "cancelled":
                order.set_cancelled()

            return Response(BaristaOrderSerializers(order).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuListApiView(APIView):
    """Представление для получения списка доступных блюд.

    Это представление позволяет только чтение (GET) и требует аутентификации пользователя.
    """
    permission_classes = [IsBarista | IsAdminUser]

    def get(self, request, *args, **kwargs):
        queryset = Menu.objects.select_related("category").prefetch_related(
            "extra_product"
        )

        user = self.request.user

        if user.branch:
            branch_id = user.branch.id
        else:
            raise Http404("Сотрудник не привязан к этому филиалу")

        category_slug = self.kwargs.get("category_slug")

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
            serializers = MenuSerializer(queryset, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)


class BaristaOrderCreateAPIView(generics.CreateAPIView):
    serializer_class = BaristaOrderSerializer
    permission_classes = [IsBarista | IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BaristaProfileAPIView(generics.ListCreateAPIView):
    serializer_class = BaristaProfileSerializer
    permission_classes = [IsBarista]

    def get_object(self):
        return self.request.user
