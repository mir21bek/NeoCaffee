# models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from branches.models import Branches
from .managers import BaseManager


class BaseUser(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ("admin", "Admin"),
        ("waiter", "Waiter"),
        ("barista", "Barista"),
        ("client", "Client"),
    ]
    login = models.CharField(max_length=100, unique=True, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(
        max_length=50,
        choices=[("waiter", "Waiter"), ("barista", "Barista")],
        blank=True,
        null=True,
    )
    branch = models.ForeignKey(
        Branches, on_delete=models.SET_NULL, null=True, blank=True
    )
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    role = models.CharField(max_length=10, choices=ROLES)
    otp = models.CharField(max_length=4, null=True, blank=True)
    is_verify = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    monday = models.BooleanField(default=False)
    monday_start_time = models.TimeField(null=True, blank=True)
    monday_end_time = models.TimeField(null=True, blank=True)

    tuesday = models.BooleanField(default=False)
    tuesday_start_time = models.TimeField(null=True, blank=True)
    tuesday_end_time = models.TimeField(null=True, blank=True)

    wednesday = models.BooleanField(default=False)
    wednesday_start_time = models.TimeField(null=True, blank=True)
    wednesday_end_time = models.TimeField(null=True, blank=True)

    thursday = models.BooleanField(default=False)
    thursday_start_time = models.TimeField(null=True, blank=True)
    thursday_end_time = models.TimeField(null=True, blank=True)

    friday = models.BooleanField(default=False)
    friday_start_time = models.TimeField(null=True, blank=True)
    friday_end_time = models.TimeField(null=True, blank=True)

    saturday = models.BooleanField(default=False)
    saturday_start_time = models.TimeField(null=True, blank=True)
    saturday_end_time = models.TimeField(null=True, blank=True)

    sunday = models.BooleanField(default=False)
    sunday_start_time = models.TimeField(null=True, blank=True)
    sunday_end_time = models.TimeField(null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = BaseManager()

    def __str__(self):
        return f" Имя: {self.first_name}, Номер телефона: {self.phone_number}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
