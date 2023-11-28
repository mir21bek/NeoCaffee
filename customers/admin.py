from django.contrib import admin
from .models import CustomerUser, WaiterUser, BaristaUser, Role

admin.site.register(CustomerUser)
admin.site.register(WaiterUser)
admin.site.register(BaristaUser)
admin.site.register(Role)
