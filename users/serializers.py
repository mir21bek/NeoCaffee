from rest_framework import serializers

from .models import StaffUser


class StaffUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = StaffUser
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Пароль не совпадает попробуйте еще раз'})
        return attrs

    def create(self, validated_data):
        username = validated_data['username']
        user = StaffUser.objects.create_user(username=username)
        user.set_password(validated_data['password'])
        user.save()

    def update(self, instance, validated_data):
        instance.username = validated_data('username', instance.username)
        instance.save()
        return instance
