from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
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


#
#
# class LoginWaiterView(generics.GenericAPIView):
#     serializer_class = WaiterLoginSerializer
#
#     def post(self, request):
#         login = request.data.get("login", "")
#
#         try:
#             user = WaiterUser.objects.get(login=login)
#
#             if not user.is_verify:
#                 otp_service = OTPService()
#                 otp_service.generate_and_send_otp(user)
#
#                 return Response(
#                     {
#                         "message": "Verification code has been sent to your phone number."
#                     },
#                     status=status.HTTP_200_OK,
#                 )
#
#         except ObjectDoesNotExist:
#             return Response(
#                 {"error": "User with this login does not exist. "},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#
#
class CustomerCheckOTPView(generics.GenericAPIView):
    serializer_class = CustomerCheckOTPSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp = serializer.validated_data["otp"]
        user = BaseUser.objects.filter(otp=otp, is_verify=False).first()

        otp_service = OTPService()
        return otp_service.check_and_activate_user(user, otp)


#
#
# class CheckOTPViewForWaiter(generics.GenericAPIView):
#     serializer_class = WaiterCheckOTPSerializer
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         otp = serializer.validated_data["otp"]
#         user = WaiterUser.objects.filter(otp=otp, is_verify=False).first()
#
#         otp_service = OTPService()
#         return otp_service.check_and_activate_user(user, otp)
#
#
# class BaristaLoginView(generics.GenericAPIView):
#     serializer_class = BaristaLoginSerializer
#
#     def post(self, request):
#         phone_number = request.data.get("phone_number")
#
#         try:
#             user = BaristaUser.objects.get(phone_number=phone_number)
#
#             if not user.is_verify:
#                 otp_service = OTPService()
#                 otp_service.generate_and_send_otp(user)
#
#             return Response(
#                 {"message": "Verification code has been sent to your phone number."},
#                 status=status.HTTP_200_OK,
#             )
#
#         except ObjectDoesNotExist:
#             return Response(
#                 {"error": "User with this phone number does not exist. "},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#
#
# class BaristaCheckOTPView(generics.GenericAPIView):
#     serializer_class = BaristaLoginSerializer
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         otp = serializer.validated_data["otp"]
#         user = BaristaUser.objects.filter(otp=otp, is_verify=False).first()
#
#         otp_service = OTPService()
#         return otp_service.check_and_activate_user(user, otp)
#
#


class CustomerProfileView(generics.ListAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = CustomerProfileSerializer

    # def get_queryset(self):
    #     return BaseUser.objects.filter(id=self.request.user.id, role='client')
