from django.contrib import admin
from .models import Branches, CoffeeShop


@admin.register(CoffeeShop)
class BranchesAdmin(admin.ModelAdmin):
    filter_horizontal = ("category", "menu")


admin.site.register(Branches)
