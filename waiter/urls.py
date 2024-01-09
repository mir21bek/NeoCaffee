from django.urls import path
from waiter.views import (
    WaiterProfileView,
    WaiterCategoriesView,
    WaiterMenuView,
    TableListView,
    OrderCreateView,
    OrderListView,
)

urlpatterns = [
    path("waiter/profile/", WaiterProfileView.as_view(), name="waiter-profile"),
    path("waiter/categories/", WaiterCategoriesView.as_view(), name="category-list"),
    path(
        "waiter/menu/<slug:category_slug>/",
        WaiterMenuView.as_view(),
        name="waiter-menu-by-category-slug",
    ),
    path("waiter/tables/", TableListView.as_view(), name="table-list"),
    path("waiter/order/create/", OrderCreateView.as_view(), name="order-create"),
    #path("waiter/order/list/", OrderListView.as_view(), name="order-list"),
]
