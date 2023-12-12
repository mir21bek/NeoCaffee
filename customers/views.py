from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status, permissions, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import BaseUser
from .services import OTPService
from .serializers import (
    CustomerRegistrationSerializer,
    CustomerCheckOTPSerializer,
    CustomerLoginSerializer,
    CustomerProfileSerializer,
)
from .utils import generate_otp, send_otp


class CustomerRegistrationView(generics.GenericAPIView):
    serializer_class = CustomerRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        otp = generate_otp()
        user.otp = otp
        user.save()

        send_otp(user.phone_number, otp)

        return Response(
            {"message": "Verification code has been sent to your phone number."},
            status=status.HTTP_200_OK,
        )


class CustomerLoginView(generics.GenericAPIView):
    serializer_class = CustomerLoginSerializer

    def post(self, request):
        phone_number = request.data.get("phone_number")

        try:
            user = BaseUser.objects.get(phone_number=phone_number)

            refresh = RefreshToken.for_user(user)
            return Response(
                {"refresh": str(refresh), "access": str(refresh.access_token)},
                status=status.HTTP_200_OK,
            )

        except ObjectDoesNotExist:
            return Response(
                {"error": "User with this phone number does not exist. "},
                status=status.HTTP_404_NOT_FOUND,
            )


class CustomerCheckOTPView(generics.GenericAPIView):
    serializer_class = CustomerCheckOTPSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp = serializer.validated_data["otp"]
        user = BaseUser.objects.filter(otp=otp, is_verify=False).first()

        otp_service = OTPService()
        return otp_service.check_and_activate_user(user, otp)


class CustomerProfileView(viewsets.ModelViewSet):
    serializer_class = CustomerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BaseUser.objects.filter(id=self.request.user.id, role="client")
