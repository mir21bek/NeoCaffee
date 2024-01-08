from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["menu"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "created")
    list_filter = ("created",)
    inlines = [OrderItemInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if "bonuses_used" in form.changed_data:
            obj.apply_bonuses(obj.bonuses_used)
