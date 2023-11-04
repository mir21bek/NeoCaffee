from rest_framework import generics, permissions, viewsets
from .models import Category, Menu, ExtraItem
from .serializers import CategorySerializer, MenuSerializer, ExtraItemSerializer
from .signals import post_category_save, post_menu_save


class CategoryApiView(generics.ListAPIView):
    """Представление для получения списка всех категорий.

    Это представление позволяет только чтение (GET) и требует аутентификации пользователя.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryCreateApiView(viewsets.ModelViewSet):
    """Представление для создания, обновления, удаления и получения категорий.

    Это представление позволяет создавать (POST), обновлять (PUT, PATCH), удалять (DELETE) и
    получать (GET) объекты категорий. Требует прав администратора для выполнения операций изменения.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        """Метод для создания новой категории и вызова сигнала после успешного создания."""
        category_instance = serializer.save()
        post_category_save(sender=Category, instance=category_instance, created=True)


class MenuListApiView(generics.ListAPIView):
    """Представление для получения списка доступных блюд.

    Это представление позволяет только чтение (GET) и требует аутентификации пользователя.
    """
    queryset = Menu.objects.all().filter(available=True)
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuCreateUpdateApiView(viewsets.ModelViewSet):
    """Представление для создания, обновления, удаления и получения блюд.

    Это представление позволяет создавать (POST), обновлять (PUT, PATCH), удалять (DELETE) и
    получать (GET) объекты блюд. Требует прав администратора для выполнения операций изменения.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        """Метод для создания нового блюда и вызова сигнала после успешного создания."""
        menu_instance = serializer.save()
        post_menu_save(sender=Menu, instance=menu_instance, created=True)


class ExtraItemViewSet(viewsets.ModelViewSet):
    queryset = ExtraItem.objects.all()
    serializer_class = ExtraItemSerializer
    permission_classes = [permissions.IsAdminUser]
