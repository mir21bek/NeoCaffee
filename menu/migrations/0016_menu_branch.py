# Generated by Django 4.2.6 on 2024-01-06 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0009_alter_branches_options'),
        ('menu', '0015_alter_category_unique_together_remove_menu_branch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='branches.branches', verbose_name='Филиал'),
        ),
    ]