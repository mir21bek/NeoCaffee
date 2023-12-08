from decimal import Decimal
from django.db import models

from order.models import Order, OrderItem
from .managers import BaseManager, CustomerManager
from .services import validate_phone_number
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)

    REQUIRED_FIELDS = []

    objects = BaseManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Управляющий"
        verbose_name_plural = "Управляющий"


class CustomerUser(models.Model):
    username = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=17, validators=[validate_phone_number], unique=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    otp = models.CharField(max_length=4, null=True, blank=True)
    is_verify = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.phone_number}"

    objects = CustomerManager()

    USERNAME_FIELD = "phone_number"

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиент"


class CustomerProfile(models.Model):
    user = models.ForeignKey(
        CustomerUser, on_delete=models.CASCADE, related_name="customer_profile"
    )
    bonuses = models.PositiveIntegerField(null=True, blank=True)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

    def bonuses_added(self):
        return self.orders.bonuses_added if self.orders else Decimal("0")

    def use_bonuses(self, amount):
        if self.bonuses >= amount:
            self.bonuses -= amount
        else:
            raise ValueError("Недостаточно бонусов")
        self.save()

    def get_all_orders(self):
        return OrderItem.objects.filter(order__user=self.user)
