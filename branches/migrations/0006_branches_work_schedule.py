# Generated by Django 4.2.6 on 2023-12-14 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0005_branches_map_link_alter_branches_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='branches',
            name='work_schedule',
            field=models.CharField(choices=[('work_day', 'С 08:00 до 00:00'), ('day_off', 'Выходной')], default='work_day', max_length=20, null=True),
        ),
    ]