from django.urls import path

from .views import *

urlpatterns = [
    path('create-staff-user/', StaffUserListCreateApi.as_view(), name='create-staff-user'),
    path('signup/', signup),
    path('login/', login),
]
