from Postsapp import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('Usersapp/',include('Usersapp.urls')),
    path('Postsapp/',include('Postsapp.urls')),
]
