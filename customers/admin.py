from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import BaseUser


@admin.register(BaseUser)
class UserAdminModel(ModelAdmin):
    list_display = (
        "first_name",
        "position",
        "role",
        "login",
        "phone_number",
        "date_of_birth",
    )
