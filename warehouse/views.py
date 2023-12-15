from rest_framework import generics
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from branches.models import Branches
from django.shortcuts import get_object_or_404


class InventoryItemListCreateView(generics.ListCreateAPIView):
    serializer_class = InventoryItemSerializer

    def get_queryset(self):
        branch_id = self.kwargs["branch_id"]
        branch = get_object_or_404(Branches, id=branch_id)
        return InventoryItem.objects.filter(branch=branch)

    def perform_create(self, serializer):
        branch_id = self.kwargs["branch_id"]
        branch = get_object_or_404(Branches, id=branch_id)
        serializer.save(branch=branch)


class InventoryItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def get_object(self):
        branch_id = self.kwargs["branch_id"]
        inventory_item_id = self.kwargs["pk"]
        branch = get_object_or_404(Branches, id=branch_id)
        return get_object_or_404(InventoryItem, id=inventory_item_id, branch=branch)
