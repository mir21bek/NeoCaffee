from django.db import models
from menu.models import Menu, Category


class Branches(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название филиала")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone_number = models.CharField(max_length=13, verbose_name="Телефон номер")
    map_link = models.URLField(verbose_name="Ссылка на 2GIS", null=True, blank=True)
    image = models.ImageField(upload_to="media/image_branches", verbose_name="Фото")

    monday = models.BooleanField(default=False)
    monday_start_time = models.TimeField(null=True, blank=True)
    monday_end_time = models.TimeField(null=True, blank=True)

    tuesday = models.BooleanField(default=False)
    tuesday_start_time = models.TimeField(null=True, blank=True)
    tuesday_end_time = models.TimeField(null=True, blank=True)

    wednesday = models.BooleanField(default=False)
    wednesday_start_time = models.TimeField(null=True, blank=True)
    wednesday_end_time = models.TimeField(null=True, blank=True)

    thursday = models.BooleanField(default=False)
    thursday_start_time = models.TimeField(null=True, blank=True)
    thursday_end_time = models.TimeField(null=True, blank=True)

    friday = models.BooleanField(default=False)
    friday_start_time = models.TimeField(null=True, blank=True)
    friday_end_time = models.TimeField(null=True, blank=True)

    saturday = models.BooleanField(default=False)
    saturday_start_time = models.TimeField(null=True, blank=True)
    saturday_end_time = models.TimeField(null=True, blank=True)

    sunday = models.BooleanField(default=False)
    sunday_start_time = models.TimeField(null=True, blank=True)
    sunday_end_time = models.TimeField(null=True, blank=True)


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
