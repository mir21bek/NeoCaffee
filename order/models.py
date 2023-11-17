from decimal import Decimal

from django.db import models
from customers.models import User
from menu.models import Menu, ExtraItem


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        order_items = self.items.all()
        total_cost = sum(item.get_cost() for item in order_items)
        return total_cost


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='order_items')
    extra_product = models.ForeignKey(ExtraItem, on_delete=models.CASCADE, null=True, related_name='extra_order')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        menu_cost = max(Decimal('0'), self.menu.price) * self.quantity
        extra_cost = max(Decimal('0'), self.extra_product.price) * self.quantity if self.extra_product else Decimal('0')
        return menu_cost + extra_cost
