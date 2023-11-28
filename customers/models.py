from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from order.models import OrderItem
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
    AbstractUser,
)
from .services import validate_phone_number


class BaseManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        phone_number = validate_phone_number(phone_number)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(phone_number, password, **extra_fields)


class BaseUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        validators=[validate_phone_number],
        max_length=17,
        unique=True,
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = BaseManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number


class CustomerUser(BaseUser):
    full_name = models.CharField(max_length=50)
    otp = models.PositiveIntegerField(null=True, blank=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name


class WaiterUser(BaseUser):
    login = models.CharField(max_length=50, null=True, unique=True)
    otp = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.login


class BaristaUser(BaseUser):
    full_name = models.CharField(max_length=50)
    otp = models.PositiveIntegerField(null=True, blank=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name


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
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=17)
    date_of_birth = models.DateField()
    schedule = models.DateField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.user}"

    class Meta:
        ordering = ["full_name"]
        indexes = [
            models.Index(fields=["role"]),
            models.Index(fields=["full_name"]),
            models.Index(fields=["-created_at"]),
        ]


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        CustomerUser, on_delete=models.CASCADE, related_name="customer_profile"
    )
    orders = models.ManyToManyField(OrderItem, related_name="customer_orders")
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=17, null=True)
    date_of_birth = models.DateField()
    bonuses = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.user}"

    class Meta:
        ordering = ["full_name"]
        indexes = [
            models.Index(fields=["full_name"]),
            models.Index(fields=["-created_at"]),
        ]
