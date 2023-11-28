from django.urls import path
from .views import CustomerRegistrationView, CheckOTPView, CustomerLoginView

urlpatterns = [
    path(
        "customers/register/",
        CustomerRegistrationView.as_view(),
        name="customers-register",
    ),
    path(
        "check-verification-code/",
        CheckOTPView.as_view(),
        name="check-code",
    ),
    path(
        "customer/login/",
        CustomerLoginView.as_view(),
        name="customer-login",
    ),
]
