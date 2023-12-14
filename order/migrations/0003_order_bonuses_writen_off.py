# Generated by Django 4.2.6 on 2023-12-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_remove_orderitem_staff"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="bonuses_writen_off",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=10,
                null=True,
                verbose_name="бонусы для списания",
            ),
        ),
    ]