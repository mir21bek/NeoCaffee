from rest_framework import serializers
from .models import StaffUser


class StaffUserSerializers(serializers.ModelSerializer):
    """
    Сериализатор для модели StaffUser.
    Позволяет валидировать и обрабатывать данные для создания и обновления пользователей.
    """
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = StaffUser
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        """
        Проверяет, совпадают ли пароли 'password' и 'password2'.
        Если не совпадают, вызывает исключение ValidationError.
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match. Please try again.'})
        return attrs

    def create(self, validated_data):
        """
        Создает нового пользователя StaffUser с указанным именем пользователя и паролем.
        """
        username = validated_data['username']
        user = StaffUser.objects.create_user(username=username)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Обновляет существующего пользователя StaffUser с новыми данными.
        """

        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance
