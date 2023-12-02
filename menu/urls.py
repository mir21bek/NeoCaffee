from django.urls import path
from rest_framework import routers
from .views import *

# Инициализация маршрутизатора для автоматической генерации URL-путей на основе представлений ViewSet
# router = routers.DefaultRouter()
# router.register("create-category", CategoryCreateApiView, basename="create-category")
# router.register("create-menu", MenuCreateUpdateApiView, basename="create-menu")
# router.register("extra-item", ExtraItemViewSet, basename="extra-item")

# URL-пути, связанные с обычными представлениями (не ViewSet)
urlpatterns = [
    path("list-category/", CategoryApiView.as_view(), name="list-category"),
    path("menu-list/<str:category_slug>/", MenuListApiView.as_view(), name="menu-list"),
    path("populars/", PopularDishesView.as_view(), name="popular-dishes"),
]

# Добавление URL-путей, сгенерированных маршрутизатором
# urlpatterns += router.urls
