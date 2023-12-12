from rest_framework import permissions, mixins, generics
from rest_framework.response import Response

from .models import Branches
from menu.models import Menu, Category
from menu.serializers import MenuSerializer, CategorySerializer
from .serializers import BranchesSerializer


class ListBranchesAPIView(generics.ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    permission_classes = [permissions.IsAuthenticated]


class BranchesDetailAPIView(generics.RetrieveAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        category = instance.branches.values_list("category", flat=True).distinct()
        category_serializer = CategorySerializer(
            Category.objects.filter(id__in=category), many=True
        )

        menus = instance.branches.values_list("menu", flat=True).distinct()
        menus_serializer = MenuSerializer(Menu.objects.filter(id__in=menus), many=True)

        return Response(
            {"menus": menus_serializer.data, "category": category_serializer.data}
        )
