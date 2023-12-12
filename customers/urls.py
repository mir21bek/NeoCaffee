from django.urls import path
from .views import (
    CustomerRegistrationView,
    CustomerCheckOTPView,
    CustomerLoginView,
    CustomerProfileView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"customer/profile/", CustomerProfileView, basename="customer/profile/")

urlpatterns = [
    path(
        "customers/register/",
        CustomerRegistrationView.as_view(),
        name="customers-register",
    ),
    path(
        "customer/check-verification-code/",
        CustomerCheckOTPView.as_view(),
        name="check-code",
    ),
    path(
        "customer/login/",
        CustomerLoginView.as_view(),
        name="customer-login",
    ),
]

urlpatterns += router.urls
