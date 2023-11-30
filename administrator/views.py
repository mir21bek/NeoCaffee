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
