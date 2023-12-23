from django.db import models
from menu.models import Menu
from warehouse.models import InventoryItem


class Ingredients(models.Model):
    UNIT_CHOICES = [
        ("kg", "кг"),
        ("g", "г"),
        ("l", "л"),
        ("ml", "мл"),
        ("unit", "шт"),
    ]
    product = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, related_name='menu_ingredients', on_delete=models.CASCADE)
    quantity_used = models.PositiveIntegerField()
    unit = models.CharField(max_length=5, choices=UNIT_CHOICES)

    class Meta:
        unique_together = ('menu_item', 'product',)

    def __str__(self):
        return f"{self.product} - {self.quantity_used} {self.get_unit_display()} использовано {self.menu_item}"
