from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order


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

