# Generated by Django 4.2.6 on 2023-12-29 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_alter_category_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='menu',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='category',
            name='branch',
        ),
    ]