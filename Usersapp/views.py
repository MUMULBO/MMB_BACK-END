from django.shortcuts import redirect, render
from .forms import CreateUserForm, UserForm
from django.contrib import auth
from rest_framework.views import APIView
# from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
# from serializers import UserSerializer
from rest_framework.authtoken.models import Token
from Usersapp.models import User


class Accounts(APIView):
    def Signup(request):
        form=CreateUserForm
        if request.method=="POST":
            data=request.POST
            if User.objects.filter(email=data['email']).exists():
                return render(request, 'Usersapp/badlogin.html')
            user=User.objects.create_user(
                email=data['email'],
                password=data['password'],
                nickname=data['nickname'],
            )
            if user is not None:
                auth.login(request, user)            
                token=Token.objects.create(user=user)
                return render(request, 'Postsapp/index.html',{'Token':token.key})        
        return render(request, 'Usersapp/signup.html', {'form':form})

    def Login(request):
        form=UserForm
        if request.method =="POST":
            email=request.POST['email']
            password=request.POST['password']
            user=auth.authenticate(request,email=email, password=password)
            
            if user is not None:
                token=Token.objects.get(user=user)
                auth.login(request, user)
                return render(request, 'Postsapp/index.html',{"Token":token.key})
        return render(request, 'Usersapp/login.html',{'form':form})
    
    def Logout(request):
        auth.logout(request)
        return redirect('/')
    
    
    
    
    
    
    
    
    
    
    
    
    