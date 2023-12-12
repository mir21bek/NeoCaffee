from django.urls import path
from .views import *

urlpatterns = [
    path("admin/login/", AdminLoginView.as_view(), name="admin-login"),
    # path("waiter/login/", LoginWaiterView.as_view(), name="waiter-login"),
    # path(
    #     "waiter/check-verification-code/",
    #     CheckOTPViewForWaiter.as_view(),
    #     name="check-code-for-waiter",
    # ),
    # path(
    #     "barista/login/",
    #     BaristaLoginView.as_view(),
    #     name="barista-login",
    # ),
    # path(
    #     "barista/check-verification-code/",
    #     BaristaCheckOTPView.as_view(),
    #     name="check-code-for-barista",
    # ),
]
