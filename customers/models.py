from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import Group, Permission


class UserManager(BaseUserManager):

    def create_user(self, name, phone_number, password=None):
        user = self.model(name=name, phone_number=phone_number)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, phone_number, password=None):
        user = self.create_user(name=name, phone_number=phone_number)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True, db_index=True)
    date_of_birth = models.DateField(null=True)
    otp = models.PositiveIntegerField(null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='user_custom',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='user_custom_permissions',
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return f"{self.phone_number}, {self.name}"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
