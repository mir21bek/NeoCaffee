from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def order_post_save(sender, instance, created, **kwargs):
    if (
        instance.order.status == "completed"
        and instance.order.user
        and instance.order.user.role == "client"
    ):
        instance.apply_cashback()
