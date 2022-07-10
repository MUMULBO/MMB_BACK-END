from django.urls import path
from . import views

app_name='Authapp'
urlpatterns = [
    path('auth/nick_check/', views.NickCheck.as_view()),
    path('auth/email_check', views.EmailCheck.as_view()),
    path('signup/', views.SignUp.as_view()),
]