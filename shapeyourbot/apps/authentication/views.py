from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, ChangePasswordSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        saved_account = serializer.save()
        token, create = Token.objects.get_or_create(user=saved_account)
        data = {
            "token": token.key,
            "username": saved_account.username,
            "email": saved_account.email
        }
        return Response(data)
    

class ChangePasswordView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['post'] 

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, create = Token.objects.get_or_create(user=user)
        data = {
            "token": token.key,
            "username": user.username,
            "email": user.email
        }
        return Response(data)
