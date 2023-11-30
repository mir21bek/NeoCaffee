from django.urls import path
from .views import *

urlpatterns = [
    path("admin/login/", AdminLoginView.as_view(), name="admin-login"),
]
