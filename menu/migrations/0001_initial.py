# Generated by Django 4.2.6 on 2023-11-29 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="Название категории"),
                ),
                ("slug", models.SlugField(max_length=200, unique=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="media/category_images",
                        verbose_name="Фото категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("slug", models.SlugField(max_length=200)),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="media/food_image",
                        verbose_name="Фото блюды",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=7, verbose_name="Цена"
                    ),
                ),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="В наличии"),
                ),
                (
                    "popular",
                    models.BooleanField(default=False, verbose_name="Популярные"),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="menus",
                        to="menu.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Меню",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="ExtraItem",
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
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="Название доп. продукта"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=7, verbose_name="Цена"
                    ),
                ),
                (
                    "choice_category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="extra_products",
                        to="menu.category",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Доп. Продукты",
                "ordering": ["name"],
            },
        ),
        migrations.AddIndex(
            model_name="category",
            index=models.Index(fields=["name"], name="menu_catego_name_dba8c8_idx"),
        ),
        migrations.AddIndex(
            model_name="menu",
            index=models.Index(fields=["id", "slug"], name="menu_menu_id_c6debc_idx"),
        ),
        migrations.AddIndex(
            model_name="menu",
            index=models.Index(fields=["name"], name="menu_menu_name_4933c0_idx"),
        ),
        migrations.AddIndex(
            model_name="menu",
            index=models.Index(
                fields=["-created"], name="menu_menu_created_8af8e3_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="extraitem",
            index=models.Index(fields=["name"], name="menu_extrai_name_315e3d_idx"),
        ),
    ]
