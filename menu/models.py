from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(max_length=200)
    image = models.ImageField(
        upload_to="media/category_images",
        verbose_name="Фото категории",
        null=True,
        blank=True,
    )
    branch = models.ForeignKey(
        "branches.Branches",
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Филиал",
        related_name="categories",
    )

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Категория",
        related_name="menus",
    )
    extra_product = models.ManyToManyField("ExtraItem", blank=True)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="media/food_image", verbose_name="Фото блюды", null=True, blank=True
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    available = models.BooleanField(default=True, verbose_name="В наличии")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    branch = models.ForeignKey(
        "branches.Branches",
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Филиал",
        related_name="menus",
    )

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]
        verbose_name_plural = "Меню"

    def __str__(self):
        return f"{self.category}: {self.name}"


class ExtraItem(models.Model):
    TYPE_CHOICE = (["Milk", "Молоко"], ["Syrop", "Сиропы"])
    choice_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="extra_products", null=True
    )
    type_extra_product = models.CharField(
        max_length=20, choices=TYPE_CHOICE, null=True, verbose_name="Доп. Продукт"
    )
    name = models.CharField(max_length=100, verbose_name="Название доп. продукта")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]
        verbose_name_plural = "Доп. Продукты"

    def __str__(self):
        return self.name
