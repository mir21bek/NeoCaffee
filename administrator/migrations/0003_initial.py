# Generated by Django 4.2.6 on 2023-12-12 23:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("administrator", "0002_delete_adminuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuIngredient",
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
                ("name", models.CharField(max_length=200)),
                ("quantity", models.IntegerField()),
                (
                    "measurement_unit",
                    models.CharField(
                        choices=[
                            ("kg", "Kilogram"),
                            ("g", "Gram"),
                            ("ml", "Milliliter"),
                            ("l", "Liter"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]
