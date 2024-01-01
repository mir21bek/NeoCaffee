from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Branches


@admin.register(Branches)
class BranchesAdminModel(ModelAdmin):
    list_display = ("name", "phone_number", "address")
