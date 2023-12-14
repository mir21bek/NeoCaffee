from django.urls import path
from .views import OrderDetail, UpdateOrderStatusView

urlpatterns = [
    path("orders/", OrderDetail.as_view()),
    path('status/<int:order_id>/<str:new_status>/', UpdateOrderStatusView.as_view()),
]
