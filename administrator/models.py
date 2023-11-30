from django.db import models


class AdminUser(models.Model):
    full_name = models.CharField(max_length=100)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return self.full_name
