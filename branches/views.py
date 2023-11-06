from rest_framework import viewsets
from rest_framework import permissions, generics

from .models import Branches, CoffeeShop
from .serializers import BranchesSerializer, CoffeeShopSerializer


class BranchesListAPI(generics.ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    permission_classes = [permissions.IsAdminUser]


class CoffeeShopListAPI(generics.ListAPIView):
    queryset = CoffeeShop.objects.all()
    serializer_class = CoffeeShopSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class CoffeeShopViewSet(viewsets.ModelViewSet):
    queryset = CoffeeShop.objects.all()
    serializer_class = CoffeeShopSerializer
    # permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = CoffeeShop.objects.all()
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
            return queryset
