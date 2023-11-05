from django.urls import path

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('create-staff-profile', StaffUserProfileApiView)
router.register('work-schedule', WorkScheduleViewSet)
router.register('month-schedule', MonthScheduleViewSet)
router.register('staff-position', StaffPositionViewSet)

urlpatterns = [
    path('signup-staff-user/', StaffUserCreateApi.as_view(), name='create-staff-user'),
    path('login-staff-user/', StaffUserLogin.as_view(), name='login-staff-user'),
    path('staff-logout/', StaffUserLogout.as_view(), name='staff-logout')
]

urlpatterns += router.urls
