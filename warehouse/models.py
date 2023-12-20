from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from branches.models import Branches


class InventoryItem(models.Model):
    MEASUREMENT_UNIT_CHOICES = [
        ("kg", "кг"),
        ("g", "г"),
        ("l", "л"),
        ("ml", "мл"),
        ("unit", "шт"),
    ]
    CATEGORY_CHOICES = [
        ("ready_products", "Готовые продукты"),
        ("raw_materials", "Сырье"),
        ("running_out", "Заканчивающиеся продукты"),
    ]

    name = models.CharField(max_length=100, verbose_name="Наименование")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    quantity_unit = models.CharField(
        max_length=20,
        choices=MEASUREMENT_UNIT_CHOICES,
        verbose_name="Единица измерения (Количество)",
    )
    limit = models.PositiveIntegerField(default=0, verbose_name="Лимит")
    arrival_date = models.DateField(verbose_name="Дата прихода")
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, verbose_name="Категория"
    )
    branch = models.ForeignKey(
        Branches, on_delete=models.CASCADE, verbose_name="Филиал"
    )
    is_running_out = models.BooleanField(
        default=False, verbose_name="Заканчивающийся продукт"
    )

    class Meta:
        ordering = ["-arrival_date", "name"]
        verbose_name_plural = "Склад"

    def __str__(self):
        return f"{self.name} ({self.get_category_display()}) {self.branch}"


@receiver(pre_save, sender=InventoryItem)
def check_running_out(sender, instance, **kwargs):
    if instance.quantity <= instance.limit:
        instance.category = "running_out"
        instance.is_running_out = True
    else:
        instance.is_running_out = False
