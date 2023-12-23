from django.contrib import admin

from .models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter


class BranchFilter(SimpleListFilter):
    title = _("branch")
    parameter_name = "branch"

    def lookups(self, request, model_admin):
        branches = set([c.branch for c in model_admin.model.objects.all()])
        return [(b.id, b.name) for b in branches]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(branch__id=self.value())
        return queryset


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "branch", "slug")
    prepopulated_fields = {"slug": ("name",)}
    list_filter = (BranchFilter,)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "category",
        "branch",
        "price",
        "available",
        "created",
    )
    filter_horizontal = ["extra_product"]
    list_filter = ("available", "created", "updated", BranchFilter)
    list_editable = ("price", "available")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ExtraItem)
class ExtraItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "type_extra_product")
    list_filter = ("name", "price")
