# Generated by Django 4.2.6 on 2023-12-16 13:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0012_baseuser_last_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="baseuser",
            old_name="full_name",
            new_name="first_name",
        ),
    ]