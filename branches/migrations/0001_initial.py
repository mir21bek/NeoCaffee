# Generated by Django 4.2.6 on 2023-11-06 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0005_extraproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Филиалы')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Телефон номер')),
                ('work_schedule', models.DateTimeField(verbose_name='График работы')),
                ('image', models.ImageField(upload_to='media/image_branches', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='branches.branches', verbose_name='Филиал')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coffee_shop', to='menu.category', verbose_name='Категория')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='menu.menu', verbose_name='Меню')),
            ],
        ),
    ]