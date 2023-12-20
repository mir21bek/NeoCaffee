from rest_framework import generics
from rest_framework.response import Response

from .models import Branches
from menu.models import Menu, Category
from menu.serializers import MenuSerializer, CategorySerializer
from .serializers import BranchesSerializer
from administrator.permissions import IsClientUser


class ListBranchesAPIView(generics.ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    permission_classes = [IsClientUser]


class BranchesDetailAPIView(generics.RetrieveAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    permission_classes = [IsClientUser]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()

        menus = Menu.objects.filter(branch=instance).distinct()
        category = Category.objects.filter(branch=instance).distinct()

        menus_serializer = MenuSerializer(menus, many=True)
        categories_serializer = CategorySerializer(category, many=True)

        return Response(
            {"menus": menus_serializer.data, "categories": categories_serializer.data}
        )
