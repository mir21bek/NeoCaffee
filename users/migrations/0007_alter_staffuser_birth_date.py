# Generated by Django 4.2.6 on 2023-10-31 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_staffuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffuser',
            name='birth_date',
            field=models.DateField(default='2000-09-12', verbose_name='Дата рождения'),
        ),
    ]