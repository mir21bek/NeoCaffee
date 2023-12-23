from django.urls import path
from .views import *


urlpatterns = [
    path(
        "list-category/<int:branch_id>/",
        CategoryApiView.as_view(),
        name="list-category",
    ),
    path(
        "list-menu/<int:branch_id>/",
        MenuApiView.as_view(),
        name="list-menu",
    ),
    path(
        "menu-list/<str:category_slug><int:branch_id>/",
        MenuListApiView.as_view(),
        name="menu-list",
    ),
    path("populars/<int:branch_id>/", PopularDishesView.as_view(), name="popular-dishes"),
]
