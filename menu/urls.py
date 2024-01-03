from django.urls import path
from .views import *


urlpatterns = [
    path(
        "list-category/",
        CategoryApiView.as_view(),
        name="list-category",
    ),
    path(
        "list-menu/",
        MenuApiView.as_view(),
        name="list-menu",
    ),
    path(
        "menu-list/<str:category_slug>/",
        MenuListApiView.as_view(),
        name="menu-list",
    ),
    path("populars/", PopularDishesView.as_view(), name="popular-dishes"),
]
