from django.urls import path
from .views import InventoryItemListCreateView, InventoryItemRetrieveUpdateDestroyView

urlpatterns = [
    path('branches/<int:branch_id>/inventory/', InventoryItemListCreateView.as_view(), name='inventory-list-create'),
    path('branches/<int:branch_id>/inventory/<int:pk>/', InventoryItemRetrieveUpdateDestroyView.as_view(), name='inventory-retrieve-update-destroy'),
]
