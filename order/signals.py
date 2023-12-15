from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order


@receiver(post_save, sender=Order)
def order_post_save(sender, instance, created, **kwargs):
    if (
        instance.status == Order.status == "completed"
        and instance.paid
        and instance.user
        and instance.user.role == "client"
    ):
        instance.get_cashback()
