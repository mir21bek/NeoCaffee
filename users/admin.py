from django.contrib import admin
from users.models import *


@admin.register(StaffUser)
class StaffUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_active", "phone_number")


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ["user", "date", "shift_type"]


@admin.register(MonthlyWorkSchedule)
class MonthlyWorkScheduleAdmin(admin.ModelAdmin):
    list_display = ["user", "month"]
    filter_horizontal = ["schedule"]


@admin.register(StaffPosition)
class StaffPositionAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(StaffUsersProfile)
class StaffUsersProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "surname"]
