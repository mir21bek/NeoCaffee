# Generated by Django 4.2.6 on 2024-01-09 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0017_category_branch"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("order", "0005_order_table_order_waiter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="customer_orders",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="extra_product",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="extra_product",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="extra_order", to="menu.extraitem"
            ),
        ),
    ]