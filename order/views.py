from rest_framework import generics, permissions, viewsets

from administrator.permissions import IsClientUser
from .serializers import OrderSerializer
from .models import Order


class OrderDetail(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsClientUser]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
