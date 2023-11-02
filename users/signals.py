from django.dispatch import receiver
from django.db.models.signals import post_save

from users.models import StaffUser


@receiver(post_save, sender=StaffUser, dispatch_uid='unique_identifier')
def post_user_save(sender, instance, created, **kwargs):
    if created:
        print(F'Пользователь с именем {instance.username} создан')
