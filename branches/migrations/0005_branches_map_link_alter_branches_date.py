# Generated by Django 4.2.6 on 2023-12-14 00:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("branches", "0004_remove_branches_work_schedule_branches_friday_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="branches",
            name="map_link",
            field=models.URLField(blank=True, null=True, verbose_name="Ссылка на 2GIS"),
        ),
        migrations.AlterField(
            model_name="branches",
            name="date",
            field=models.DateField(
                blank=True, null=True, verbose_name="График работы: Выберите дату"
            ),
        ),
    ]
