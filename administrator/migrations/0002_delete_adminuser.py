# Generated by Django 4.2.6 on 2023-12-12 17:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("administrator", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AdminUser",
        ),
    ]
