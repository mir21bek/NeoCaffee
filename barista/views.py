from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from administrator.permissions import IsBarista, IsAdminUser
from order.models import Order
from drf_yasg.utils import swagger_auto_schema
from .serializers import BaristaOrderSerializers, OrderStatusUpdateSerializer


class OrdersView(APIView):
    def get(self, request, *args, **kwargs):
        status = request.query_params.get("status", None)
        order_type = request.query_params.get("type", None)

        orders = Order.objects.all()
        if status:
            orders = orders.filter(status=status)
        if order_type:
            orders = orders.filter(order_type=order_type)
        orders = orders.order_by("-created")

        serializer = BaristaOrderSerializers(orders, many=True)
        return Response(serializer.data)


class UpdateStatusAPIView(APIView):
    permission_classes = [IsBarista | IsAdminUser]

    @swagger_auto_schema(request_body=OrderStatusUpdateSerializer)
    def post(self, request, *args, **kwargs):
        serializer = OrderStatusUpdateSerializer(data=request.data)
        if serializer.is_valid():
            order_id = serializer.validated_data["order_id"]
            new_status = serializer.validated_data["new_status"]
            try:
                order = Order.objects.get(id=order_id)
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
