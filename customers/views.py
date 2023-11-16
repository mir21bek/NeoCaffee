from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from .utils import generate_otp, send_otp
from .models import User
from .serializers import (RegistrationSerializer,
                          LoginSerializer,
                          CheckOPTSerializer,
                          ProfileSerializer,
                          LogoutSerializer)


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        otp = generate_otp()
        user.otp = otp
        user.save()

        send_otp(user.username, otp)

        return Response({'message': 'Verification code has been sent to your phone number.'}, status=status.HTTP_200_OK)


class CheckOTPView(generics.GenericAPIView):
    serializer_class = CheckOPTSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp = serializer.validated_data['otp']
        user = User.objects.filter(otp=otp, is_verified=False).first()

        if not user:
            raise exceptions.APIException('Code is incorrect!')

        if not user.is_verified:
            user.is_verified = True
            user.otp = None
            user.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {'message': 'User is already verified.'}, status=status.HTTP_400_BAD_REQUEST
            )



class LoginView(APIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: 'OK', 404: 'Not Found'},
    )
    def post(self, request):
        username = request.data.get('phone_number', '')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User with this phone number does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if user.otp:
            user.otp = None
            user.save()

        otp = generate_otp()
        user.otp = otp
        user.save()

        send_otp(username, otp)

        return Response({'message': 'One-time password has been sent to your phone number.'}, status=status.HTTP_200_OK)


class LoginCheckOTPView(generics.GenericAPIView):
    serializer_class = CheckOPTSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            otp = serializer.validated_data['otp']
            user = User.objects.filter(otp=otp).first()
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                })
            return Response({'detail': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
