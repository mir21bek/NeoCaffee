from django.urls import path

from barista.views import OrdersView, UpdateStatusAPIView, BaristaProfileAPIView

urlpatterns = [
    path("orders/", OrdersView.as_view()),
    path("orders/update_status/", UpdateStatusAPIView.as_view()),
    path("barista/profile/", BaristaProfileAPIView.as_view()),
]
