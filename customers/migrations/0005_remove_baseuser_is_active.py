# Generated by Django 4.2.6 on 2023-11-30 14:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0004_alter_baristauser_user_alter_customeruser_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="baseuser",
            name="is_active",
        ),
    ]