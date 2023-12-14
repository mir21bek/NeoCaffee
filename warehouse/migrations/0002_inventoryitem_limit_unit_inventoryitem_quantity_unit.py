# Generated by Django 4.2.6 on 2023-12-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='limit_unit',
            field=models.CharField(choices=[('kg', 'Килограмм'), ('g', 'Грамм'), ('l', 'Литр'), ('ml', 'Миллилитр'), ('unit', 'Штука')], default=1, max_length=20, verbose_name='Единица измерения (Лимит)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='quantity_unit',
            field=models.CharField(choices=[('kg', 'Килограмм'), ('g', 'Грамм'), ('l', 'Литр'), ('ml', 'Миллилитр'), ('unit', 'Штука')], default=1, max_length=20, verbose_name='Единица измерения (Количество)'),
            preserve_default=False,
        ),
    ]
