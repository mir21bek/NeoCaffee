# Generated by Django 4.2.6 on 2023-11-06 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_monthlyworkschedule_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlyworkschedule',
            options={'verbose_name_plural': 'График работы на месяц'},
        ),
        migrations.AlterModelOptions(
            name='staffposition',
            options={'verbose_name_plural': 'Должность сотрудников'},
        ),
        migrations.AlterModelOptions(
            name='workschedule',
            options={'verbose_name_plural': 'График работы сотрудников'},
        ),
    ]
