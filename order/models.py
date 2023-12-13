from decimal import Decimal
from django.db import models
from django.conf import settings
from branches.models import Branches
from menu.models import Menu, ExtraItem


class Order(models.Model):
    NEW, IN_PROCESS, DONE, CANCELLED, COMPLETED = (
        "Новый",
        "В процессе",
        "Готово",
        "Отменено",
        "Завершено",
    )
    StatusChoice = [
        (NEW, "Новый"),
        (IN_PROCESS, "В процессе"),
        (DONE, "Готово"),
        (CANCELLED, "Отменено"),
        (COMPLETED, "Завершено"),
    ]

    status = models.CharField(max_length=20, choices=StatusChoice, default=NEW)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="customer_orders",
        null=True,
        blank=True,
    )
    menu = models.ManyToManyField("menu.Menu", through="OrderItem")
    extra_products = models.ManyToManyField("menu.ExtraItem", through="OrderItem")
    bonuses_writen_off = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="бонусы для списания",
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    branch = models.ForeignKey(
        "branches.Branches", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["-created"])]

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return max(total_cost - self.bonuses_writen_off, Decimal("0.00"))

    def get_cashback(self):
        if self.status == self.COMPLETED:
            total_cost = self.get_total_cost()
            cashback = total_cost * Decimal("0.05")
            if self.user and self.user.role == "client":
                self.user.bonuses += cashback
                self.user.save()
            return cashback
        return Decimal("0.00")

    def apply_bonuses(self, bonuses_amount):
        if self.user.bonuses < bonuses_amount:
            raise ValueError("Недостаточно бонусов")
        self.user.bonuses -= bonuses_amount
        self.bonuses_writen_off = bonuses_amount
        self.user.save()
        self.save()

        total_cost = self.get_total_cost()
        return max(total_cost, Decimal("0.00"))

    def update_status(self, new_status):
        if new_status in [self.IN_PROCESS, self.DONE, self.CANCELLED, self.COMPLETED]:
            self.status = new_status
            self.save()
        else:
            raise ValueError("Неверный статус заказа.")


class OrderItem(models.Model):
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
        return f"OrderItem {self.id}"

    def get_cost(self):
        menu_cost = max(Decimal("0"), self.menu.price) * int(self.menu_quantity)
        extra_cost = (
            max(Decimal("0"), self.extra_product.price)
            * int(self.extra_product_quantity)
            if self.extra_product
            else Decimal("0")
        )
        return menu_cost + extra_cost
