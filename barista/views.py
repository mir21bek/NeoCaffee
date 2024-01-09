from django.http import Http404
from drf_yasg import openapi
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from administrator.permissions import IsBarista, IsAdminUser, IsWaiter
from menu.models import Menu
from menu.serializers import MenuSerializer
from order.models import Order, OrderItem
from drf_yasg.utils import swagger_auto_schema
from .serializers import (
    BaristaOrderSerializers,
    OrderStatusUpdateSerializer,
    BaristaProfileSerializer,
    BaristaOrderSerializer,
    BaristaMenuDetailSerializer,
    BaristaOrderDetailSerializer,
)


class OrdersView(APIView):
    permission_classes = [IsBarista | IsAdminUser]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "status",
                openapi.IN_QUERY,
                description="Статус заказа",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "order_type",
                openapi.IN_QUERY,
                description="Тип заказа",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        user_branch = request.user.branch
        type_status = request.query_params.get("status", None)
        order_type = request.query_params.get("order_type", None)

        orders = Order.objects.all()
        if status:
            orders = orders.filter(status=type_status, user_branch=user_branch)
        if order_type:
            orders = orders.filter(order_type=order_type)
        orders = orders.order_by("-created")

        serializer = BaristaOrderSerializers(orders, many=True)
        return Response(serializer.data)


class BaristaOrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsBarista | IsAdminUser]
    serializer_class = BaristaOrderDetailSerializer
    lookup_field = "id"


class BaristaOrderChangeDetailAPIView(APIView):
    permission_classes = [IsBarista | IsAdminUser]

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Http404

    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = BaristaOrderDetailSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            return Response(
                {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
            )


class BaristaMenuDetailAPIView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = BaristaMenuDetailSerializer
    permission_classes = [IsBarista | IsAdminUser]
    lookup_field = "id"


class BaristaOrderCreateAPIView(generics.CreateAPIView):
    serializer_class = BaristaOrderSerializer
    permission_classes = [IsBarista | IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BaristaProfileAPIView(generics.ListAPIView):
    serializer_class = BaristaProfileSerializer
    permission_classes = [IsBarista]

    def get_object(self):
        return self.request.user
