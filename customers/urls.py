from django.urls import path
from .views import (
    CustomerRegistrationView,
    CustomerCheckOTPView,
    CustomerLoginView,
    LoginWaiterView,
    CheckOTPViewForWaiter,
    BaristaLoginView,
    BaristaCheckOTPView,
)

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
    path("waiter/login/", LoginWaiterView.as_view(), name="waiter-login"),
    path(
        "waiter/check-verification-code/",
        CheckOTPViewForWaiter.as_view(),
        name="check-code-for-waiter",
    ),
    path(
        "barista/login/",
        BaristaLoginView.as_view(),
        name="barista-login",
    ),
    path(
        "barista/check-verification-code/",
        BaristaCheckOTPView.as_view(),
        name="check-code-for-barista",
    ),
]
