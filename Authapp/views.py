# Create your views here.
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.http import Http404
from django.core.mail import EmailMessage
import random
from django.contrib import auth
from .models import User
from . import serializers
from Postsapp.models import Majors
from argon2 import PasswordHasher
import bcrypt

class NickCheck(APIView):
    def post(self, request):
        request_nickname = request.data['nickname']

        if User.objects.filter(nickname = request_nickname).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_200_OK)

class EmailCheck(APIView):
    def post(self, request):
        request_email = request.data['email']

        if User.objects.filter(email = request_email).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            access_code = random.randrange(1000, 9999)
            email = EmailMessage(
                "MUMULBO 회원가입 인증코드입니다.",
                "인증코드 : " + str(access_code),
                to = [request_email+'@kumoh.ac.kr']
            )
            email.send()
            return Response({'code' : access_code}, status=status.HTTP_200_OK)

class SignUp(APIView):
    def post(self, request):
        major = Majors.objects.get(id=request.data['major_id'])
        if major:
            user = User.objects.create_user(
                email = request.data['email'] + '@kumoh.ac.kr',
                password = request.data['password'],
                nickname = request.data['nickname'],
                major_id = major,
            )
        if user is not None:
            Token.objects.create(user = user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class LogIn(APIView):
    def post(self, request):
        request_email = request.data['email']
        request_password = request.data['password']

        if User.objects.filter(email = request_email).exists():
            user = User.objects.get(email = request_email)
            
            if bcrypt.checkpw(request_password.encode('utf-8'), user.password.encode('utf-8')) :

                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)




