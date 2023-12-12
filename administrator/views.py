from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from .permissions import IsAdminUser

from customers.services import OTPService
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist


class AdminLoginView(generics.GenericAPIView):
    serializer_class = AdminLoginSerializer

    def post(self, request):
        login = request.data.get("login", "")

        try:
            user = BaseUser.objects.get(login=login)

            if not user.is_verify:
                if user.position == "admin":
                    otp_service = OTPService()
                    otp_service.generate_and_send_otp(user)

                return Response(
                    {
                        "message": "Verification code has been sent to your phone number."
                    },
                    status=status.HTTP_200_OK,
                )

        except ObjectDoesNotExist:
            return Response(
                {"error": "User with this login does not exist. "},
                status=status.HTTP_404_NOT_FOUND,
            )


class LoginWaiterView(generics.GenericAPIView):
    serializer_class = WaiterLoginSerializer

    def post(self, request):
        login = request.data.get("login", "")

        try:
            user = BaseUser.objects.get(login=login)

            if not user.is_verify:
                if user.position == "waiter":
                    otp_service = OTPService()
                    otp_service.generate_and_send_otp(user)

                return Response(
                    {
                        "message": "Verification code has been sent to your phone number."
                    },
                    status=status.HTTP_200_OK,
                )

        except ObjectDoesNotExist:
            return Response(
                {"error": "User with this login does not exist. "},
                status=status.HTTP_404_NOT_FOUND,
            )


class CheckOTPViewForWaiter(generics.GenericAPIView):
    serializer_class = WaiterCheckOTPSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp = serializer.validated_data["otp"]
        user = BaseUser.objects.filter(otp=otp, is_verify=False).first()

        otp_service = OTPService()
        return otp_service.check_and_activate_user(user, otp)


class BaristaLoginView(generics.GenericAPIView):
    serializer_class = BaristaLoginSerializer

    def post(self, request):
        phone_number = request.data.get("phone_number")

        try:
            user = BaseUser.objects.get(phone_number=phone_number)

            if not user.is_verify:
                if user.position == "barista":
                    otp_service = OTPService()
                    otp_service.generate_and_send_otp(user)

            return Response(
                {"message": "Verification code has been sent to your phone number."},
                status=status.HTTP_200_OK,
            )

        except ObjectDoesNotExist:
            return Response(
                {"error": "User with this phone number does not exist. "},
                status=status.HTTP_404_NOT_FOUND,
            )


class BaristaCheckOTPView(generics.GenericAPIView):
    serializer_class = BaristaLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp = serializer.validated_data["otp"]
        user = BaseUser.objects.filter(otp=otp, is_verify=False).first()

        otp_service = OTPService()
        return otp_service.check_and_activate_user(user, otp)


class StaffProfileAPIView(viewsets.ModelViewSet):
    serializer_class = StaffProfileSerializer
    permission_classes = [IsAdminUser]
    queryset = BaseUser.objects.all()
