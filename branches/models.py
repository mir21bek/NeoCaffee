from django.db import models

from menu.models import Menu, Category


class Branches(models.Model):
    name = models.CharField(max_length=100, verbose_name='Филиалы')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone_number = models.CharField(max_length=13, verbose_name='Телефон номер')
    work_schedule = models.DateTimeField(verbose_name='График работы')
    image = models.ImageField(upload_to='media/image_branches', verbose_name='Фото')

    def __str__(self):
        return self.name


class CoffeeShop(models.Model):
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE,
                               related_name='branches', verbose_name='Филиал')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория', related_name='coffee_shop')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,
                             related_name='menu', verbose_name='Меню')

    def __str__(self):
        return self.branch
