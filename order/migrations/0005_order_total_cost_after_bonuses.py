# Generated by Django 4.2.6 on 2023-12-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0004_order_is_processed"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_cost_after_bonuses",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
