from django.db import models

from menu.models import Menu, Category


class Branches(models.Model):
    name = models.CharField(max_length=100, verbose_name="Филиалы")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone_number = models.CharField(max_length=13, verbose_name="Телефон номер")
    date = models.DateField(verbose_name="График работы: Выберите дату", null=True)
    WORK_DAY = "work_day"
    DAY_OFF = "day_off"

    SHIFT_CHOICES = [
        (WORK_DAY, "С 08:00 до 00:00"),
        (DAY_OFF, "Выходной"),
    ]
    work_schedule = models.CharField(
        max_length=20, choices=SHIFT_CHOICES, default=WORK_DAY, null=True
    )
    image = models.ImageField(upload_to="media/image_branches", verbose_name="Фото")

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
