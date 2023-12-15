from django.urls import path
from .views import OrderDetail

urlpatterns = [
    path("orders/", OrderDetail.as_view()),
]
