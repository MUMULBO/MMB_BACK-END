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
        serializer = serializers.UserSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registred a new user"
            data['email'] = account.email
            data['nickname'] = account.nickname
            data['major_id'] = account.major_id
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


        # user=User.objects.create_user(
        #     email=request.data['email'],
        #     password=request.data['password'],
        #     nickname=request.data['nickname'],
        #     # major_id=request.data['major_id'],
        # )
        
        # if user is not None:
        #     auth.login(request, user)   
        #     Token.objects.create(user=user)
        #     return Response(status=status.HTTP_200_OK)
        # return Response(status=status.HTTP_400_BAD_REQUEST)



