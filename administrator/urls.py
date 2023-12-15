from django.urls import path
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"staff/profile", StaffProfileAPIView, basename="staff-profile")

urlpatterns = [
    path("admin/login/", AdminLoginView.as_view(), name="admin-login"),
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
    path("category/", CategoryListCreateView.as_view(), name="category-create"),
    path("category/<int:pk>/", CategoryDeleteView.as_view(), name="category-delete"),
    path("menu/create/", MenuCreateView.as_view(), name="menu-create"),
    path("branches/", BranchListCreateView.as_view(), name="branch-list-create"),
    path("branches/<int:id>/", BranchDetailView.as_view(), name="branch-detail"),
    path("staff/create", StaffCreateView.as_view(), name="staff-create"),
    path(
        "staff/branch/<int:branch_id>/", StaffByBranchView.as_view(), name="staff-list"
    ),
    path("staff/<int:id>/", StaffDetailView.as_view(), name="employee-detail"),
]

urlpatterns += router.urls
