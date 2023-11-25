from django.db import models
from django.core.validators import RegexValidator
from order.models import OrderItem
from django.contrib.auth.models import User


class CustomerUser(models.Model):
    full_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex='^\+?1?\d(9,15)$', message="Номер телефона должен быть в формате: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    otp = models.PositiveIntegerField(max_length=4)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'full_name'
    REQUIRED_FIELD = ['phone_number']

    def __str__(self):
        return self.full_name


class WaiterUser(models.Model):
    login = models.CharField(max_length=50, null=True, unique=True)
    otp = models.PositiveIntegerField(max_length=4)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['login']


class AdminUser(models.Model):
    login = models.CharField(max_length=50, null=True, unique=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['login']


class BaristaUser(models.Model):
    full_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex='^\+?1?\d(9,15)$', message="Номер телефона должен быть в формате: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    otp = models.PositiveIntegerField(max_length=4)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'full_name'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.full_name


class Role(models.Model):
    class ChoiceRole(models.TextChoices):
        BARISTA = "BARISTA" 'Barista'
        WAITER = "WAITER" 'Waiter'

    role = models.CharField(max_length=20, choices=ChoiceRole.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role


class StaffUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role')
    login = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=17)
    date_of_birth = models.DateField()
    schedule = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User {self.user}"

    class Meta:
        ordering = 'name'
        index = [
            models.Index(fields=['role']),
            models.Index(fields=['name']),
            models.Index(fields=['-created_at']),
        ]


class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomerUser, on_delete=models.CASCADE, related_name='customer_profile')
    orders = models.ManyToManyField(OrderItem, related_name='customer_orders')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=17, null=True)
    date_of_birth = models.DateField()
    bonuses = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"User {self.user}"

    class Meta:
        ordering = 'full_name'
        index = [
            models.Index(fields=['full_name']),
            models.Index(fields=['-created_at']),
        ]
