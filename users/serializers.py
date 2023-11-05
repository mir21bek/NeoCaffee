from rest_framework import serializers
from .models import *


class StaffUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = StaffUser
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Создает нового пользователя StaffUser с указанным именем пользователя и паролем.
        """
        user = StaffUser.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        return user

    def update(self, instance, validated_data):
        """
        Обновляет существующего пользователя StaffUser с новыми данными.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance


class StaffUsersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffUsersProfile
        fields = "__all__"

    def create(self, validated_data):
        profile = StaffUsersProfile.objects.create(**validated_data)
        return profile

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.image = validated_data.get('image', instance.image)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.residential_address = validated_data.get('residential_address', instance.residential_address)
        instance.home_number = validated_data.get('home_number', instance.home_number)
        instance.password_image = validated_data.get('password_image', instance.password_image)
        instance.work_schedule = validated_data.get('work_schedule', instance.work_schedule)
        instance.is_admin_user = validated_data.get('is_admin_user', instance.is_admin_user)
        instance.save()
        return instance

    def __delete__(self, instance):
        instance.delete()


class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = ('user', 'date', 'shift_type')


class MonthlyScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyWorkSchedule
        fields = ('user', 'month', 'schedule')


class StaffPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPosition
        fields = ('user', 'name')
