# Generated by Django 4.2.6 on 2023-12-14 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("menu", "0004_merge_20231214_2231"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("branches", "0007_remove_branches_work_schedule_alter_branches_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "Новый"),
                            ("in_process", "В процессе"),
                            ("done", "Готово"),
                            ("cancelled", "Отменено"),
                            ("completed", "Завершено"),
                        ],
                        default="new",
                        max_length=20,
                    ),
                ),
                (
                    "order_type",
                    models.CharField(
                        choices=[("takeaway", "На вынос"), ("inplace", "В заведении")],
                        default="takeaway",
                        max_length=20,
                    ),
                ),
                (
                    "uniq_order_number",
                    models.UUIDField(
                        blank=True,
                        default=uuid.uuid4,
                        editable=False,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "bonuses_writen_off",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                        verbose_name="бонусы для списания",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "branch",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="branches.branches",
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("menu_quantity", models.PositiveIntegerField(default=1)),
                ("extra_product_quantity", models.PositiveIntegerField(default=1)),
                (
                    "extra_product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="extra_order",
                        to="menu.extraitem",
                    ),
                ),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_items",
                        to="menu.menu",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="order.order",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="extra_products",
            field=models.ManyToManyField(
                through="order.OrderItem", to="menu.extraitem"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="menu",
            field=models.ManyToManyField(through="order.OrderItem", to="menu.menu"),
        ),
        migrations.AddField(
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
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["-created"], name="order_order_created_708daa_idx"
            ),
        ),
    ]
