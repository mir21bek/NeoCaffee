# Generated by Django 4.2.6 on 2023-11-15 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_extraitem_alter_category_options_alter_menu_options_and_more'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='extra_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_order', to='menu.extraitem'),
        ),
    ]
