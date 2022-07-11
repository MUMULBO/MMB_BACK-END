from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Authapp/',include('Authapp.urls')),
    path('Postsapp/',include('Postsapp.urls')),
]
