from django.urls import path
from Usersapp.views import Accounts

app_name='Usersapp'
urlpatterns=[
    path('login/',Accounts.Login, name='login'),
    path('signup/',Accounts.Signup, name='signup'),
]