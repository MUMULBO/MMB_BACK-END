from django.shortcuts import render
from .forms import PostForm

def home(request):
    return render(request, 'Postsapp/index.html')

def upload(request):
    form=PostForm
    return render(request, 'Postsapp/upload.html',{'form':form})