from django.urls import path
from .views import OrderListCreateView, OrderUpdateView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view()),
    path('orders/<int:pk>/', OrderUpdateView.as_view()),
]
