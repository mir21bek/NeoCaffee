from django.db import models
from django.contrib.auth.models import AbstractUser


class StaffUser(AbstractUser):
    username = models.CharField(max_length=150, verbose_name='Логин', unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    USERNAME_FIELD = 'username'


class StaffPosition(models.Model):
    user = models.ForeignKey(StaffUser, on_delete=models.CASCADE,
                             verbose_name='Сотрудник', related_name='staff_position')
    name = models.CharField(max_length=100, verbose_name='Должность сотрудника')

    class Meta:
        verbose_name_plural = 'Должность сотрудников'

    def __str__(self):
        return self.name


class WorkSchedule(models.Model):
    DAY_SHIFT = 'day_shift'
    NIGHT_SHIFT = 'night_shift'
    DAY_OFF = 'day_off'

    SHIFT_CHOICES = [
        (DAY_SHIFT, 'Дневная смена с 10:00 до 17:00'),
        (NIGHT_SHIFT, 'Вечерняя смена с 17:00 до 23:00'),
        (DAY_OFF, 'Выходной'),
    ]

    position = models.ForeignKey(StaffPosition, on_delete=models.CASCADE, verbose_name='Должность', null=True)
    user = models.ForeignKey(StaffUser, on_delete=models.CASCADE, verbose_name='сотрудник', related_name='work_schedule')
    date = models.DateField(verbose_name='График работы')
    shift_type = models.CharField(max_length=20, choices=SHIFT_CHOICES, verbose_name='Выберите смену')

    class Meta:
        verbose_name_plural = 'График работы сотрудников'
        unique_together = ('user', 'date')

    def __str__(self):
        return f"Дни {self.date}"


class MonthlyWorkSchedule(models.Model):
    position = models.ForeignKey(StaffPosition, on_delete=models.CASCADE, verbose_name='Должность', null=True)
    user = models.ForeignKey(StaffUser, on_delete=models.CASCADE, verbose_name='сотрудник', related_name='monthly_work_schedule')
    month = models.DateField()
    schedule = models.ManyToManyField(WorkSchedule, verbose_name='График')

    class Meta:
        verbose_name_plural = 'График работы на месяц'
        unique_together = ('user', 'month')

    def __str__(self):
        return f"График {self.schedule}"


class StaffUsersProfile(models.Model):
    user = models.OneToOneField(StaffUser, on_delete=models.CASCADE, related_name='profile', null=True)
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')
    image = models.ImageField(upload_to='media/staff_images', verbose_name='Фото')
    birth_date = models.DateField(verbose_name='Дата рождения', default='2000-09-12')
    residential_address = models.CharField(max_length=255, verbose_name='Адрес проживвание')
    home_number = models.CharField(max_length=150, verbose_name='Номер дома')
    password_image = models.ImageField(upload_to='media/staff_password_image', verbose_name='Фото паспорта')
    work_schedules = models.ManyToManyField(WorkSchedule, verbose_name='График работы', related_name='profiles')
    is_admin_user = models.BooleanField(default=False, verbose_name='Администратор')

    def __str__(self):
        return f"ФИО сотрудника {self.name} {self.surname} "

    class Meta:
        verbose_name = 'Профиль Сотрудника'
        verbose_name_plural = 'Профиль Сотрудников'
