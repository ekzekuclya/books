from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django_filters import exceptions
from rest_framework import generics, response, status, exceptions
from django.contrib.auth.models import User
from .serializers import RegUserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class RegUserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegUserSerializer
    permission_classes = [AllowAny]     # Исключение Auth


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]     # Исключение auth

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,   # Сериализируем данные юзера
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])

        if not user:
            raise exceptions.AuthenticationFailed()
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])

        token, _ = Token.objects.get_or_create(user=user)

        return response.Response(data={"token": token.key},
                                 status=status.HTTP_200_OK)
