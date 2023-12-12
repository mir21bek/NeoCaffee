from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import *
from .models import AdminUser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken


class AdminLoginView(generics.GenericAPIView):
    serializer_class = AdminLoginSerializer

    def post(self, request):
        login = request.data.get("login")

        try:
            user = AdminUser.objects.get(login=login)

            if not user.login:
                return Response(
                    {
                        "error": "With this login user does not exist. Please contact with base manager"
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
            else:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {"refresh": str(refresh), "access": str(refresh.access_token)},
                    status=status.HTTP_200_OK,
                )

        except ObjectDoesNotExist:
            return Response(
                {"error" "Credential error in service"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
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
