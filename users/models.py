from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class StaffUser(AbstractUser):
    username = models.CharField(max_length=150, verbose_name='Логин', unique=True)
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')
    image = models.ImageField(upload_to='media/staff_images', verbose_name='Фото')
    birth_date = models.DateField(verbose_name='Дата рождения', default='2000-09-12')
    residential_address = models.CharField(max_length=255, verbose_name='Адрес проживвание')
    home_number = models.CharField(max_length=150, verbose_name='Номер дома')
    password_image = models.ImageField(upload_to='media/staff_password_image', verbose_name='Фото паспорта')
    work_schedule = models.DateField(verbose_name='График работы', null=True, blank=True)

    def __str__(self):
        return f"ФИО сотрудника {self.name} {self.surname} "

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    USERNAME_FIELD = 'username'




