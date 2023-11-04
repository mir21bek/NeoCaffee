from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/food_image', verbose_name='Фото блюды', null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    popular = models.BooleanField(default=False, verbose_name='Популярные')

    def __str__(self):
        return f"{self.category}: {self.name}"


class ExtraItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название доп. продукта')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name


class ExtraProduct(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    extra = models.ForeignKey(ExtraItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
