from django.urls import path
from .views import OrderHistory, OrderCreateAPIView

urlpatterns = [
    path("order/history/", OrderHistory.as_view()),
    path("create/order/", OrderCreateAPIView.as_view()),
]
