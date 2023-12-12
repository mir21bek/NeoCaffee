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
    login = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    position = models.CharField(
        max_length=50,
        choices=[("waiter", "Waiter"), ("barista", "Barista")],
        blank=True,
        null=True,
    )
    DAY_SHIFT = "day_shift"
    NIGHT_SHIFT = "night_shift"
    DAY_OFF = "day_off"

    SHIFT_CHOICES = [
        (DAY_SHIFT, "Дневная смена с 10:00 до 17:00"),
        (NIGHT_SHIFT, "Вечерняя смена с 17:00 до 23:00"),
        (DAY_OFF, "Выходной"),
    ]
    date = models.DateField(verbose_name="График работы", null=True, blank=True)
    monday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    tuesday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    wednesday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    thursday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    friday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    saturday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    sunday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    branch = models.ForeignKey(
        Branches, on_delete=models.SET_NULL, null=True, blank=True
    )
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    role = models.CharField(max_length=10, choices=ROLES, default="client")
    otp = models.CharField(max_length=4, null=True, blank=True)
    is_verify = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = BaseManager()

    def __str__(self):
        return f" ФИО: {self.username}, Номер телефона: {self.phone_number}"

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользовател"
