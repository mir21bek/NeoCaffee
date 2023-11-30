from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from order.models import OrderItem
from .managers import UserManager
from .services import validate_phone_number
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    username = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(
        validators=[validate_phone_number], max_length=17, unique=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    otp = models.CharField(max_length=4, null=True, blank=True)
    is_verify = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.phone_number) if self.phone_number else f"User {self.id}"

    class Meta:
        verbose_name = "Управляющий"
        verbose_name_plural = "Управляющий"


class CustomerUser(BaseUser):
    user = models.ForeignKey(
        BaseUser,
        on_delete=models.CASCADE,
        related_name="customers",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.phone_number}"

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиент"


class BaristaUser(BaseUser):
    user = models.ForeignKey(
        BaseUser,
        on_delete=models.CASCADE,
        related_name="barista",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.phone_number}"

    class Meta:
        verbose_name = "Бариста"
        verbose_name_plural = "Бариста"


class WaiterUser(BaseUser):
    user = models.ForeignKey(
        BaseUser,
        on_delete=models.CASCADE,
        related_name="waiters",
        null=True,
        blank=True,
    )
    login = models.CharField(max_length=50, null=True, unique=True)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = "Официанты"
        verbose_name_plural = "Официант"


class Role(models.Model):
    class ChoiceRole(models.TextChoices):
        BARISTA = "BARISTA", "Barista"
        WAITER = "WAITER", "Waiter"

    role = models.CharField(max_length=20, choices=ChoiceRole.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role


class StaffUserProfile(models.Model):
    user_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    user_id = models.PositiveIntegerField()
    user = GenericForeignKey("user_type", "user_id")
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    login = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=17)
    date_of_birth = models.DateField()
    schedule = models.DateField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.user}"

    class Meta:
        ordering = ["username"]
        indexes = [
            models.Index(fields=["role"]),
            models.Index(fields=["username"]),
            models.Index(fields=["-created_at"]),
        ]


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        BaseUser, on_delete=models.CASCADE, related_name="customer_profile"
    )
    orders = models.ManyToManyField(OrderItem, related_name="customer_orders")
    username = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=17, null=True)
    date_of_birth = models.DateField()
    bonuses = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.user}"

    class Meta:
        ordering = ["username"]
        indexes = [
            models.Index(fields=["username"]),
            models.Index(fields=["-created_at"]),
        ]
