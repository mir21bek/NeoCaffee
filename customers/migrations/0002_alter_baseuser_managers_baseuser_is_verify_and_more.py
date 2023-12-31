# Generated by Django 4.2.6 on 2023-12-11 21:52

import customers.managers
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="baseuser",
            managers=[
                ("objects", customers.managers.BaseManager()),
            ],
        ),
        migrations.AddField(
            model_name="baseuser",
            name="is_verify",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="baseuser",
            name="otp",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
