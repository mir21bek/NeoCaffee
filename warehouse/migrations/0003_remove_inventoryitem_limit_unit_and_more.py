# Generated by Django 4.2.6 on 2023-12-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_inventoryitem_limit_unit_inventoryitem_quantity_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='limit_unit',
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='category',
            field=models.CharField(choices=[('ready_products', 'Готовые продукты'), ('raw_materials', 'Сырье')], max_length=20, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='quantity_unit',
            field=models.CharField(choices=[('kg', 'кг'), ('g', 'г'), ('l', 'л'), ('ml', 'мл'), ('unit', 'шт')], max_length=20, verbose_name='Единица измерения (Количество)'),
        ),
    ]