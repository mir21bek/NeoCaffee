from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response

from .serializers import OrderSerializer
from .models import Order


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        for order_data in serializer.data:
            order = Order.objects.get(pk=order_data['id'])
            order_data['total_cost'] = order.get_total_cost()
        return Response(serializer.data)


class OrderUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
