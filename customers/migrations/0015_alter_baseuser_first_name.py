# Generated by Django 4.2.6 on 2024-01-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0014_remove_baseuser_date_baseuser_friday_end_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="baseuser",
            name="first_name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]