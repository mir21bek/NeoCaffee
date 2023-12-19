from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "category",
        "price",
        "available",
        "created",
    )
    filter_horizontal = ["extra_product"]
    list_filter = ("available", "created", "updated")
    list_editable = ("price", "available")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ExtraItem)
class ExtraItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "type_extra_product")
    list_filter = ("name", "price")
