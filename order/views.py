from rest_framework import generics

from administrator.permissions import IsClientUser
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order


class OrderCreateAPIView(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsClientUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.order.user)


class OrderHistory(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsClientUser]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
