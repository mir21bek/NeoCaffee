from django.urls import path

from .views import *

urlpatterns = [
    path('create-staff-user/', StaffUserCreateApi.as_view(), name='create-staff-user'),
]
