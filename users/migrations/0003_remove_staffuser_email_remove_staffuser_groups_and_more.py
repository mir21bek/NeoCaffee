# Generated by Django 4.2.6 on 2023-10-31 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_login_staffuser_username_staffuser_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='staffuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='staffuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='staffuser',
            name='user_permissions',
        ),
    ]
