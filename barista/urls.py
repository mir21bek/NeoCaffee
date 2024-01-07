from django.urls import path

from barista.views import (
    OrdersView,
    UpdateStatusAPIView,
    BaristaProfileAPIView,
    MenuListApiView,
    BaristaOrderCreateAPIView,
    BaristaMenuDetailAPIView
)

urlpatterns = [
    path("orders/", OrdersView.as_view()),
    path("orders/update_status/", UpdateStatusAPIView.as_view()),
    path("barista/profile/", BaristaProfileAPIView.as_view()),
    path(
        "menu-list/<str:category_slug>/",
        MenuListApiView.as_view(),
        name="menu-list",
    ),
    path("menu-detail/<int:id>/", BaristaMenuDetailAPIView.as_view(), name="menu-detail"),
    path("order/create/", BaristaOrderCreateAPIView.as_view()),
]
