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
        "popular",
    )
    list_filter = ("available", "popular", "created", "updated")
    list_editable = ("price", "popular", "available")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ExtraItem)
class ExtraItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    list_filter = ("name", "price")
