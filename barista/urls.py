from django.urls import path

from barista.views import (
    OrdersView,
    UpdateStatusAPIView,
    BaristaProfileAPIView,
    MenuListApiView,
)

urlpatterns = [
    path("orders/", OrdersView.as_view()),
    path("orders/update_status/", UpdateStatusAPIView.as_view()),
    path("barista/profile/", BaristaProfileAPIView.as_view()),
    path(
        "menu-list/<str:category_slug><int:branch_id>/",
        MenuListApiView.as_view(),
        name="menu-list",
    ),
]
