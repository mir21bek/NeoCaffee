# Generated by Django 4.2.6 on 2023-12-11 22:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "customers",
            "0005_baseuser_groups_baseuser_is_active_baseuser_is_staff_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="baseuser",
            name="username",
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
