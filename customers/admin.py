from django.contrib import admin
from .models import BaseUser, WaiterUser, Role

admin.site.register(BaseUser)
admin.site.register(WaiterUser)
admin.site.register(Role)
