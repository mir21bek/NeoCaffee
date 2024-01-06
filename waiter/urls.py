from django.urls import path
from .views import WaiterProfileView, WaiterCategoriesView, WaiterMenuView

urlpatterns = [
    path('waiter/profile/', WaiterProfileView.as_view(), name='waiter-profile'),
    path('waiter/categories/', WaiterCategoriesView.as_view(), name='category-list'),
    path('waiter/menu/<slug:category_slug>/', WaiterMenuView.as_view(), name='waiter-menu-by-category-slug'),
]
