from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework import permissions

from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import StaffUser
from .serializers import StaffUserSerializers
from .signals import post_user_save


class StaffUserListCreateApi(generics.ListCreateAPIView):
    """
    API-представление для создания и просмотра пользователей StaffUser.
    Позволяет администраторам создавать новых пользователей и просматривать список существующих пользователей.
    """
    queryset = StaffUser.objects.all()
    serializer_class = StaffUserSerializers
    permission_classes = [permissions.IsAdminUser]


@csrf_exempt
def signup(request):
    """
    Регистрация нового пользователя StaffUser.
    Принимает данные в формате JSON с полями 'username' и 'password'.
    Возвращает токен доступа в случае успешной регистрации.
    """
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = StaffUser.objects.create_user(username=data['username'], password=data['password'])

            # Вызываем сигнал после успешного создания пользователя
            post_user_save(sender=StaffUser, instance=user, created=True)

            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'Username taken. Choose another username.'}, status=400)


@csrf_exempt
def login(request):
    """
    Вход пользователя StaffUser.
    Принимает данные в формате JSON с полями 'username' и 'password'.
    Возвращает токен доступа в случае успешного входа.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': 'Unable to login. Check username and password.'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
