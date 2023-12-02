# Generated by Django 4.2.6 on 2023-12-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0001_initial"),
        ("branches", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coffeeshop",
            name="category",
        ),
        migrations.RemoveField(
            model_name="coffeeshop",
            name="menu",
        ),
        migrations.AddField(
            model_name="coffeeshop",
            name="category",
            field=models.ManyToManyField(
                null=True,
                related_name="coffee_shop",
                to="menu.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AddField(
            model_name="coffeeshop",
            name="menu",
            field=models.ManyToManyField(
                null=True, related_name="menu", to="menu.menu", verbose_name="Меню"
            ),
        ),
    ]
