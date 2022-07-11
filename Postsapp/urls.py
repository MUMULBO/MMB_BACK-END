from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('post/', views.Postclass.as_view()),
    path('detail/<int:pk>/',views.Postdetail.as_view()),
    path('comment/',views.Commentclass.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)