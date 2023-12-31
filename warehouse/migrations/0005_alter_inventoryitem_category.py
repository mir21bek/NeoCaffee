# Generated by Django 4.2.6 on 2023-12-31 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_inventoryitem_is_running_out_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='category',
            field=models.CharField(choices=[('ready_products', 'Готовые продукты'), ('raw_materials', 'Сырье')], max_length=20, verbose_name='Категория'),
        ),
    ]
