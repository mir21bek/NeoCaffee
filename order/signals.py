from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Order, OrderItem


@receiver(post_save, sender=Order)
def order_post_save(sender, instance, created, **kwargs):
    if (
        instance.status == "completed"
        and instance.user
        and instance.user.role == "client"
        and not created
        and instance._prev_status != instance.status
    ):
        instance.apply_cashback()


@receiver(pre_save, sender=OrderItem)
def update_stock_on_order(sender, instance, **kwargs):
    """
    Обновить запасы на складе при создании заказа.
    """
    for ingredient in instance.menu.menu_ingredients.all():
        ingredient.product.decrease_stock(ingredient.quantity_used * instance.menu_quantity)
