from django.shortcuts import render

from rest_framework import generics

from .models import StaffUser
from .serializers import StaffUserSerializers


class StaffUserCreateApi(generics.CreateAPIView):
    serializer_class = StaffUserSerializers

