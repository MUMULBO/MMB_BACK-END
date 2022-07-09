from django.shortcuts import render
from .forms import PostForm
from .models import Posts
from .serializers import PostSerializer
from rest_framework import viewsets

def home(request):
    return render(request, 'Postsapp/index.html')

def upload(request):
    form=PostForm
    return render(request, 'Postsapp/upload.html',{'form':form})

class PostsViewSet(viewsets.ModelViewSet):
    queryset=Posts.objects.all();
    serializer_class=PostSerializer