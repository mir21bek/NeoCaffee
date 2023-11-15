from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class RegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='username', required=True)

    class Meta:
        model = User
        fields = ['name', 'phone_number', 'date_of_birth']

    def save(self):
        user = User(
            name=self.validated_data['name'],
            username=self.validated_data['username'],
            date_of_birth=self.validated_data['date_of_birth'])
        user.save()
        return user


class CheckOPTSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField()

    class Meta:
        model = User
        fields = ['otp']


class LoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='username', required=True, max_length=15)

    class Meta:
        model = User
        fields = ['phone_number']


class ProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='username', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'phone_number', 'date_of_birth']


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
