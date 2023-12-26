from rest_framework import generics
from rest_framework.views import APIView

from administrator.permissions import IsClientUser
from .serializers import OrderSerializer, OrderHistorySerializer


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsClientUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.order.user)


class OrderHistory(APIView):
    serializer_class = OrderHistorySerializer
    permission_classes = [IsClientUser]

    def get_queryset(self):
        return self.request.user
