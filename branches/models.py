from django.db import models
from menu.models import Menu, Category


class Branches(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название филиала")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone_number = models.CharField(max_length=13, verbose_name="Телефон номер")
    date = models.DateField(
        verbose_name="График работы: Выберите дату", null=True, blank=True
    )
    map_link = models.URLField(verbose_name="Ссылка на 2GIS", null=True, blank=True)
    image = models.ImageField(upload_to="media/image_branches", verbose_name="Фото")
    WORK_DAY = "work_day"
    DAY_OFF = "day_off"

    SHIFT_CHOICES = [
        (WORK_DAY, "С 08:00 до 00:00"),
        (DAY_OFF, "Выходной"),
    ]
    monday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    tuesday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    wednesday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    thursday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    friday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    saturday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )
    sunday = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        verbose_name="Выберите смену",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class CoffeeShop(models.Model):
    branch = models.ForeignKey(
        Branches,
        on_delete=models.CASCADE,
        related_name="branches",
        verbose_name="Филиал",
    )
    category = models.ManyToManyField(
        Category,
        verbose_name="Категория",
        related_name="coffee_shop",
    )
    menu = models.ManyToManyField(Menu, related_name="menu", verbose_name="Меню")

    def __str__(self):
        return f"{self.branch}"
