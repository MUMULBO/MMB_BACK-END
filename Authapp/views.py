# Create your views here.
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.core.mail import EmailMessage
import random
from django.contrib import auth
from .models import User
from . import serializers
from Postsapp.models import Majors


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
        major=Majors.objects.get(id=request.data['major_id'])        
        user=User.objects.create_user(email=request.data['email'], password=request.data['password'], 
major_id=major,nickname=request.data['nickname'])
        user.save()
        return Response(status=status.HTTP_200_OK)
        

class LogIn(APIView):
    def post(self, request):
        request_email = request.data['email']
        request_password = request.data['password']

        if User.objects.filter(email = request_email).exists():
            user = User.objects.get(email = request_email)
            token=Token.objects.create(user=user)
            user.token=token
            user.save() 
            return Response({'token':token}, status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)




