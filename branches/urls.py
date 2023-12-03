from django.urls import path

from . import views

urlpatterns = [
    path("list-branches/", views.ListBranchesAPIView.as_view(), name="branch-list"),
    path(
        "detail/branches/<int:pk>/",
        views.BranchesDetailAPIView.as_view(),
        name="branch-detail",
    ),
]
