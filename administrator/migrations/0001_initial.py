# Generated by Django 4.2.6 on 2023-12-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
                ("login", models.CharField(max_length=50, unique=True)),
                ("password", models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
    ]
