from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from config import settings


schema_view = get_schema_view(
    openapi.Info(
        title="This is API for future NeoCaffee CRM systems",
        default_version="v1",
        description="Please enjoy using this API end keep calm )) with love your teammates Mirbek and Asel",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("api-menu/", include("menu.urls")),
    path("api-branches/", include("branches.urls")),
    path("api-customers/", include("customers.urls")),
    path("api-admin/", include("administrator.urls")),
    path("api-order/", include("order.urls")),
    path("api-warehouse/", include("warehouse.urls")),
    path("api-barista/", include("barista.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]
