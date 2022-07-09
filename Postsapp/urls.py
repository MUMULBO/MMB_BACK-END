from django.urls import path
from Postsapp import views 

app_name='Postsapp'
urlpatterns=[
    path('upload/',views.upload, name='upload'),
]
