from django.urls import path
from .views import *


urlpatterns = [
    path(
        "list-category/<int:branch_id>/",
        CategoryApiView.as_view(),
        name="list-category",
    ),
    path(
        "menu-list/<str:category_slug><int:branch_id>/",
        MenuListApiView.as_view(),
        name="menu-list",
    ),
    path("populars/", PopularDishesView.as_view(), name="popular-dishes"),
]
