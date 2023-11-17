from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework import permissions

from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import *
from .serializers import *
from .signals import post_user_save


class StaffUserCreateApi(generics.CreateAPIView):
    """
    API-представление для создания и просмотра пользователей StaffUser.
    Позволяет администраторам создавать новых пользователей и просматривать список существующих пользователей.
    """
    def get_serializer_class(self):
        return StaffUserSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            post_user_save(sender=StaffUser, instance=user, created=True)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffUserLogin(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={200: 'Token is returned successfully', 400: 'Invalid credentials'},
    )
    def post(self, request, *args, **kwargs):
        serializer = StaffUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=request.data.get('username'),
                password=request.data.get('password')
            )
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class StaffUserLogout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request):
        request.delete()
        return Response({'message': 'Вы успешно вышли, ждем вас снова.'})


class StaffUserProfileApiView(viewsets.ModelViewSet):
    queryset = StaffUsersProfile.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = StaffUsersProfileSerializer

    def get_object(self):
        return self.request.user.profile

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class WorkScheduleViewSet(viewsets.ModelViewSet):
    queryset = WorkSchedule.objects.all()
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = WorkScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'create': 'График удачно создан'})
        else:
            return Response({'error': 'Invalid credentials'})


class MonthScheduleViewSet(viewsets.ModelViewSet):
    queryset = MonthlyWorkSchedule.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    @staticmethod
    def post(request):
        serializer = MonthlyScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'create': 'График удачно создан'})
        else:
            return Response({'error': 'Invalid credentials'})


class StaffPositionViewSet(viewsets.ModelViewSet):
    queryset = StaffPosition.objects.all()
    serializer_class = StaffPositionSerializer
    permission_classes = [permissions.IsAdminUser]
