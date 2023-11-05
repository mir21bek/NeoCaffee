from django.contrib import admin
from users.models import *


@admin.register(StaffUser)
class StaffUser(admin.ModelAdmin):
    list_display = ['username']


@admin.register(WorkSchedule)
class StaffUser(admin.ModelAdmin):
    list_display = ['user', 'date', 'shift_type']


@admin.register(MonthlyWorkSchedule)
class StaffUser(admin.ModelAdmin):
    list_display = ['user', 'month']
    filter_horizontal = ['schedule']


@admin.register(StaffPosition)
class StaffUser(admin.ModelAdmin):
    list_display = ['user', 'name']


@admin.register(StaffUsersProfile)
class StaffUser(admin.ModelAdmin):
    list_display = ['user', 'name', 'surname']
