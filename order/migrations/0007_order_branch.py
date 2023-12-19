# Generated by Django 4.2.6 on 2023-12-19 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("branches", "0007_remove_branches_work_schedule_alter_branches_name"),
        ("order", "0006_alter_orderitem_branch"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="branch",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="branches.branches",
            ),
        ),
    ]
