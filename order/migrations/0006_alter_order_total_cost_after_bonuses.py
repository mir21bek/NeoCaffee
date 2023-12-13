# Generated by Django 4.2.6 on 2023-12-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0005_order_total_cost_after_bonuses"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="total_cost_after_bonuses",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=10, null=True
            ),
        ),
    ]
