from django.contrib import admin
from .models import BaseUser, BaristaUser, CustomerUser, WaiterUser, Role

admin.site.register(BaseUser)
admin.site.register(CustomerUser)
admin.site.register(BaristaUser)
admin.site.register(WaiterUser)
admin.site.register(Role)
