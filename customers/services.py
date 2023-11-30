from django.core.validators import RegexValidator
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from customers.utils import generate_otp, send_otp


def validate_phone_number(value):
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Номер телефона должен быть в формате: '+999999999'.",
    )
    phone_regex(value)


class OTPService:
    @staticmethod
    def check_and_activate_user(user, otp):
        if user:
            if not user.is_verify:
                user.is_verify = True
                user.otp = None
                user.save()

                refresh = RefreshToken.for_user(user)
                return Response(
                    {"refresh": str(refresh), "access": str(refresh.access_token)},
                    status=status.HTTP_200_OK,
                )
        else:
            return Response(
                {"message": "User is already verified."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @staticmethod
    def generate_and_send_otp(user):
        otp = generate_otp()
        user.otp = otp
        user.save()

        send_otp(user.phone_number, otp)
