from django.contrib import admin
from .models import StaffUser


@admin.register(StaffUser)
class StaffUser(admin.ModelAdmin):
    list_display = ('username', 'name', 'surname')
