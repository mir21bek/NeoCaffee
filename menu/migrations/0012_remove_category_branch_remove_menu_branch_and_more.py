# Generated by Django 4.2.6 on 2023-12-20 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("branches", "0007_remove_branches_work_schedule_alter_branches_name"),
        ("menu", "0011_remove_category_branch_remove_menu_branch_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="branch",
        ),
        migrations.RemoveField(
            model_name="menu",
            name="branch",
        ),
        migrations.AddField(
            model_name="category",
            name="branch",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="branches.branches",
            ),
        ),
        migrations.AddField(
            model_name="menu",
            name="branch",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="branches.branches",
            ),
        ),
    ]