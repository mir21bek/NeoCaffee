# Generated by Django 4.2.6 on 2023-11-12 18:00

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StaffPosition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="Должность сотрудника"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Должность сотрудников",
            },
        ),
        migrations.AlterModelManagers(
            name="staffuser",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name="staffuser",
            old_name="login",
            new_name="username",
        ),
        migrations.RemoveField(
            model_name="staffuser",
            name="birth_date",
        ),
        migrations.RemoveField(
            model_name="staffuser",
            name="home_number",
        ),
        migrations.RemoveField(
            model_name="staffuser",
            name="image",
        ),
        migrations.RemoveField(
            model_name="staffuser",
            name="name",
        ),
        migrations.RemoveField(
            model_name="staffuser",
            name="password_image",
        ),
        migrations.RemoveField(
            model_name="staffuser",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="staffuser",
            name="residential_address",
        ),
        migrations.RemoveField(
            model_name="staffuser",
            name="surname",
        ),
        migrations.RemoveField(
            model_name="staffuser",
            name="work_schedule",
        ),
        migrations.AddField(
            model_name="staffuser",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date joined"
            ),
        ),
        migrations.AddField(
            model_name="staffuser",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
        migrations.AddField(
            model_name="staffuser",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AddField(
            model_name="staffuser",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="staffuser",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
        migrations.AddField(
            model_name="staffuser",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
        migrations.AddField(
            model_name="staffuser",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AddField(
            model_name="staffuser",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
        migrations.AddField(
            model_name="staffuser",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.CreateModel(
            name="WorkSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(verbose_name="График работы")),
                (
                    "shift_type",
                    models.CharField(
                        choices=[
                            ("day_shift", "Дневная смена с 10:00 до 17:00"),
                            ("night_shift", "Вечерняя смена с 17:00 до 23:00"),
                            ("day_off", "Выходной"),
                        ],
                        max_length=20,
                        verbose_name="Выберите смену",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.staffposition",
                        verbose_name="Должность",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="work_schedule",
                        to="users.staffuser",
                        verbose_name="сотрудник",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "График работы сотрудников",
                "unique_together": {("user", "date")},
            },
        ),
        migrations.CreateModel(
            name="StaffUsersProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Имя")),
                ("surname", models.CharField(max_length=150, verbose_name="Фамилия")),
                (
                    "phone_number",
                    models.CharField(max_length=13, verbose_name="Номер телефона"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="media/staff_images", verbose_name="Фото"
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        default="2000-09-12", verbose_name="Дата рождения"
                    ),
                ),
                (
                    "residential_address",
                    models.CharField(max_length=255, verbose_name="Адрес проживвание"),
                ),
                (
                    "home_number",
                    models.CharField(max_length=150, verbose_name="Номер дома"),
                ),
                (
                    "password_image",
                    models.ImageField(
                        upload_to="media/staff_password_image",
                        verbose_name="Фото паспорта",
                    ),
                ),
                (
                    "is_admin_user",
                    models.BooleanField(default=False, verbose_name="Администратор"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to="users.staffuser",
                    ),
                ),
                (
                    "work_schedules",
                    models.ManyToManyField(
                        related_name="profiles",
                        to="users.workschedule",
                        verbose_name="График работы",
                    ),
                ),
            ],
            options={
                "verbose_name": "Профиль Сотрудника",
                "verbose_name_plural": "Профиль Сотрудников",
            },
        ),
        migrations.AddField(
            model_name="staffposition",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staff_position",
                to="users.staffuser",
                verbose_name="Сотрудник",
            ),
        ),
        migrations.CreateModel(
            name="MonthlyWorkSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("month", models.DateField()),
                (
                    "position",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.staffposition",
                        verbose_name="Должность",
                    ),
                ),
                (
                    "schedule",
                    models.ManyToManyField(
                        to="users.workschedule", verbose_name="График"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="monthly_work_schedule",
                        to="users.staffuser",
                        verbose_name="сотрудник",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "График работы на месяц",
                "unique_together": {("user", "month")},
            },
        ),
    ]
