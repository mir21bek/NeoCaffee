from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import *


urlpatterns = [
    path("register", RegistrationView.as_view(), name="registration"),
    path("otp-check", CheckOTPView.as_view(), name="otp-check"),
    path("login", LoginView.as_view(), name="login"),
    path("login-otp-check", LoginCheckOTPView.as_view(), name="login-otp-check"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
