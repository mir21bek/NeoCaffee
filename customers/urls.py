from django.urls import path
from .views import (
    RegisterView,
    PhoneNumberVerificationCodeView,
    PhoneNumberVerificationView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "send-verification-code/",
        PhoneNumberVerificationView.as_view(),
        name="send-code",
    ),
    path(
        "check-verification-code/",
        PhoneNumberVerificationCodeView.as_view(),
        name="check-code",
    ),
]
