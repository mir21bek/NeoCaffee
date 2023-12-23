# Generated by Django 4.2.6 on 2023-12-20 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("branches", "0007_remove_branches_work_schedule_alter_branches_name"),
        ("menu", "0009_alter_menu_extra_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="branch",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="branches.branches",
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="extra_product",
            field=models.ManyToManyField(blank=True, to="menu.extraitem"),
        ),
    ]