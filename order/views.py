from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from administrator.permissions import IsClientUser
from .serializers import OrderSerializer
from .models import Order, OrderItem


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    # permission_classes = [IsClientUser]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.order.user)


class OrderHistory(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    # queryset = OrderItem.objects.all()
    # serializer_class = OrderSerializer
    # permission_classes = [IsClientUser]

    # def get_queryset(self):
    #     user = self.request.user
    #     return Order.objects.filter(user=user)
