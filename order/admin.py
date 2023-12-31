from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["menu"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "created", "updated")
    list_filter = ("created", "updated")
    inlines = [OrderItemInline]
