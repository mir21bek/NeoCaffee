# Generated by Django 4.2.6 on 2023-11-30 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="baseuser",
            name="otp",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name="baseuser",
            name="username",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="waiteruser",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="waiters",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]