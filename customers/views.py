# views.py
from allauth.account.utils import setup_user_email
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.account.models import EmailAddress
from phonenumbers import parse as parse_phone_number
from twilio.rest import Client
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import StaffUserProfile
from .serializers import (
    BaseUserUserSerializer,
    UserProfileSerializer,
    PhoneNumberVerificationSerializer,
    PhoneNumberVerificationCodeSerializer,
)
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


class RegisterView(APIView):
    @permission_classes([AllowAny])
    def post(self, request, *args, **kwargs):
        serializer = BaseUserUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            setup_user_email(request, user, [])
            EmailAddress.objects.create(
                user=user, email=user.phone_number, primary=True, verified=True
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneNumberVerificationView(APIView):
    @permission_classes([AllowAny])
    def post(self, request, *args, **kwargs):
        serializer = PhoneNumberVerificationSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = parse_phone_number(
                serializer.validated_data["phone_number"], "KG"
            )
            # Отправка кода для верификации через Twilio
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            verification = client.verify.services(
                settings.TWILIO_SERVER_SID
            ).verifications.create(
                to=f"+{phone_number.country_code}{phone_number.national_number}",
                channel="sms",
            )
            return Response({"detail": "Verification code sent successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneNumberVerificationCodeView(APIView):
    @permission_classes([AllowAny])
    def post(self, request, *args, **kwargs):
        serializer = PhoneNumberVerificationCodeSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = parse_phone_number(
                serializer.validated_data["phone_number"], "KG"
            )
            # Проверка верификации через Twilio
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            verification_check = client.verify.services(
                settings.TWILIO_SERVER_SID
            ).verification_checks.create(
                to=f"+{phone_number.country_code}{phone_number.national_number}",
                code=serializer.validated_data["code"],
            )
            if verification_check.status == "approved":
                user = get_user_model().objects.get(phone_number=phone_number)
                user.is_active = True
                user.save()
                return Response({"detail": "Phone number verified successfully."})
            return Response(
                {"detail": "Invalid verification code."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    def get(self, request, *args, **kwargs):
        user_profile = StaffUserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)
