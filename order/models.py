from decimal import Decimal

from django.db import models
from menu.models import Menu, ExtraItem
from branches.models import Branches


class Order(models.Model):
    NEW = "Новый"
    IN_PROCESS = "В процессе"
    DONE = "Готово"
    CANCELLED = "Отменено"
    COMPLETED = "Завершено"

    StatusChoice = [
        (NEW, "Новый"),
        (IN_PROCESS, "В процессе"),
        (DONE, "Готово"),
        (CANCELLED, "Отменено"),
        (COMPLETED, "Завершено"),
    ]

    status = models.CharField(max_length=20, choices=StatusChoice, default=NEW)
    user = models.ForeignKey(
        "customers.CustomerUser", on_delete=models.CASCADE, null=True, blank=True
    )
    products_menu = models.ManyToManyField(Menu, through="OrderItem")
    extra_products = models.ManyToManyField(ExtraItem, through="OrderItem")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        order_items = self.items.all()
        total_cost = sum(item.get_cost() for item in order_items)
        return total_cost

    def get_cashback(self):
        total_cost = self.get_total_cost()
        return total_cost * Decimal("0.05")

    def paid_order(self):
        return all(item.paid for item in self.items.all())

    def completed_order(self):
        if self.paid_order():
            if self.paid_order():
                cashback = self.get_cashback()
                self.status = self.COMPLETED
                self.bonuses_added = cashback
                self.save()
                return cashback

    def accept_order(self):
        if self.status == self.NEW:
            for item in self.items.all():
                if not item.menu.available:
                    raise ValueError("Некоторые продукты в заказе не в наличии. ")

            self.status = self.IN_PROCESS
            self.save()

    def mark_as_done(self):
        if self.status == self.IN_PROCESS:
            self.status = self.DONE
            self.save()

    def completed_order(self):
        if self.paid_order():
            self.status = self.COMPLETED
            self.save()

    def cancelled_order(self):
        self.status = self.CANCELLED
        self.save()


class OrderItem(models.Model):
    branch = models.ForeignKey(
        Branches, on_delete=models.CASCADE, related_name="branches_in_order", null=True
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="order_items")
    menu_quantity = models.PositiveIntegerField(default=1)
    extra_product = models.ForeignKey(
        ExtraItem,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="extra_order",
    )
    extra_product_quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        menu_cost = max(Decimal("0"), self.menu.price) * self.menu_quantity
        extra_cost = (
            max(Decimal("0"), self.extra_product.price) * self.extra_product_quantity
            if self.extra_product
            else Decimal("0")
        )
        return menu_cost + extra_cost
