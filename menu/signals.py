from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Menu, Category


@receiver(post_save, sender=Menu)
def post_menu_save(sender,  instance, created, **kwargs):
    """Это функция для сигнала при создании новой позиции в меню."""
    if created:
        print(f'Блюда добавлено: {instance.name}, Категория: {instance.category}')


@receiver(post_save, sender=Category)
def post_category_save(sender, instance, created, **kwargs):
    """Это функция для сигнала при создании новой категории."""
    if created:
        print(f'Категория добавлено: {instance.name}')
