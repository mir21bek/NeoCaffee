from django.urls import path
from rest_framework import routers
from .views import *


urlpatterns = [
    path("list-category/", CategoryApiView.as_view(), name="list-category"),
    path("menu-list/<str:category_slug>/", MenuListApiView.as_view(), name="menu-list"),
    path("populars/", PopularDishesView.as_view(), name="popular-dishes"),
    path("menu-and-extras/", MenuAndExtraItemsView.as_view(), name="menu-and-extras"),
]
