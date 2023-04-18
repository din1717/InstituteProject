from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .registerserializer import RegisterSerialaizer, LoginSerializer

class RegisterAPi(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerialaizer

class LoginView(generics.CreateAPIView):
    serializer_class= LoginSerializer
    queryset=User.objects.all()

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        if user and check_password(password,user.password):
            if user.is_active:
                login(request, user)
                return Response({"status": "User logged in succesfully"},status=status.HTTP_200_OK)
            return Response({"status": "user is not active"})
        return Response({"status":"invalid email and password"})
