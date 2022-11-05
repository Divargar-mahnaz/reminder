from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.models import Token

from apps.account.exceptions import LoginFail
from apps.account.serializer.account import LoginSerializer, RegisterSerializer
from common.base_view import NoAuthAPIView
from common.messages import USER_CREATED_SUCCESSFULLY
from common.response import Response


class RegisterAPIView(NoAuthAPIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.data)
        return Response({'message': USER_CREATED_SUCCESSFULLY}, status=status.HTTP_201_CREATED)


class LoginAPIView(NoAuthAPIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user is None:
            raise LoginFail
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
