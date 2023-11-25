from rest_framework import routers

from django.urls import path

from .views import *

router = routers.DefaultRouter()
router.register("create-update-branches", BranchesViewSet)
router.register(
    "create-update-coffeeshop", CoffeeShopViewSet, basename="create-update-coffeeshop"
)

urlpatterns = [
    path("list-branches/", BranchesListAPI.as_view()),
    path("list-coffeeshop/", CoffeeShopListAPI.as_view()),
]

urlpatterns += router.urls
