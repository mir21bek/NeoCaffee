from decimal import Decimal
from django.db import models
from django.conf import settings
from menu.models import Menu, ExtraItem
from branches.models import Branches
from waiter.models import Table
from customers.models import BaseUser
import logging

logger = logging.getLogger(__name__)


class Order(models.Model):
    TYPE_CHOICES = [
        ("takeaway", "На вынос"),
        ("inplace", "В заведении"),
    ]
    STATUS_CHOICES = [
        ("new", "Новый"),
        ("in_process", "В процессе"),
        ("done", "Готово"),
        ("cancelled", "Отменено"),
        ("completed", "Завершено"),
    ]

    order_type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default="takeaway"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="customer_orders",
        null=True,
        blank=True,
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    branch = models.ForeignKey(Branches, on_delete=models.SET_NULL, null=True)
    bonuses_used = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    waiter = models.ForeignKey(
        BaseUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"position": "waiter"},
    )
    created = models.DateTimeField(auto_now_add=True)

    _prev_status = None

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self._prev_status = self.status

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        if is_new or self.status != self._prev_status:
            super().save(*args, **kwargs)
            self.update_total_price()
            if not is_new:
                self._prev_status = self.status
                # self.notify_status_change()
        else:
            super().save(*args, **kwargs)

    def update_total_price(self):
        total_price = sum(item.get_cost() for item in self.items.all())
        amount = self.total_price = total_price
        return max(amount - self.bonuses_used, Decimal("0.00"))

    # def notify_status_change(self):
    #     if self.user:
    #         channel_layer = get_channel_layer()
    #         message = {
    #             "type": "order_status_change",
    #             "order_id": self.id,
    #             "status": self.status,
    #         }
    #
    #         async_to_sync(channel_layer.group_send)(
    #             f"user_{self.user.id}",
    #             {
    #                 "type": "websocket.send",
    #                 "text": json.dumps(message),
    #             },
    #         )

    def apply_bonuses(self, bonuses_amount):
        logger.info(
            f"Начало применения бонусов: {bonuses_amount}, текущий баланс клиента: {self.user.bonuses}"
        )
        if self.user.bonuses < bonuses_amount:
            raise ValueError("Недостаточно бонусов")
        self.user.bonuses -= bonuses_amount
        self.bonuses_used = bonuses_amount
        self.user.save()

        logger.info(f"Конец применения бонусов, новый баланс: {self.user.bonuses}")

        total_cost = self.update_total_price()
        return max(total_cost, Decimal("0.00"))

    def apply_cashback(self):
        if self.status != self._prev_status and self.status == "completed":
            total_price = self.update_total_price()
            cashback = total_price * Decimal("0.05")
            if self.user and self.user.role == "client":
                self.user.bonuses += cashback
                self.user.save()
            return cashback
        return Decimal("0.00")

    def set_in_process(self):
        if self.status == "new":
            self.status = "in_process"
            self.save()
            return True
        return False

    def set_completed(self):
        if self.status in ["new", "in_process"]:
            self.status = "completed"
            self.save()
            return True
        return False

    def set_cancelled(self):
        if self.status not in ["completed", "cancelled"]:
            self.status = "cancelled"
            self.save()
            return True
        return False

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-created"]
        indexes = [models.Index(fields=["-created"])]

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="order_items")
    menu_quantity = models.PositiveIntegerField(default=1)
    extra_product = models.ManyToManyField(
        ExtraItem,
        blank=True,
        related_name="extra_order",
    )
    extra_product_quantity = models.PositiveIntegerField(default=0)

    def get_cost(self):
        menu_cost = (
            max(Decimal("0"), self.menu.price) * self.menu_quantity
            if self.menu
            else Decimal("0")
        )
        extra_cost = (
            max(Decimal("0"), self.extra_product.price) * self.extra_product_quantity
            if self.extra_product
            else Decimal("0")
        )
        return menu_cost + extra_cost
