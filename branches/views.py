from rest_framework import viewsets
from rest_framework import permissions, generics
from rest_framework.response import Response

from .models import Branches, CoffeeShop
from menu.models import Menu, Category
from menu.serializers import MenuSerializer, CategorySerializer
from .serializers import BranchesSerializer, CoffeeShopSerializer


class BranchesListAPI(generics.ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    permission_classes = [permissions.IsAuthenticated]


class BranchesDetailAPIView(generics.ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        menus = Menu.objects.all()
        menus_serializer = MenuSerializer(menus, many=True)
        categorys = Category.objects.all()
        categorys_serializer = CategorySerializer(categorys, many=True)

        return Response({
            'menus': menus_serializer.data,
            'category': categorys_serializer.data
        })

#
# class BranchesViewSet(viewsets.ModelViewSet):
#     queryset = Branches.objects.all()
#     serializer_class = BranchesSerializer
#     permission_classes = [permissions.IsAdminUser]


class CoffeeShopListAPI(generics.ListAPIView):
    queryset = CoffeeShop.objects.all()
    serializer_class = CoffeeShopSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


# class CoffeeShopViewSet(viewsets.ModelViewSet):
#     queryset = CoffeeShop.objects.all()
#     serializer_class = CoffeeShopSerializer
    # permission_classes = [permissions.IsAdminUser]

    # def get_queryset(self):
    #     queryset = CoffeeShop.objects.all()
    #     category_id = self.request.query_params.get("category_id")
    #     if category_id:
    #         queryset = queryset.filter(category_id=category_id)
    #         return queryset
