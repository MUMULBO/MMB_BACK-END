from django.contrib import admin
from Postsapp.models import Posts
from Usersapp.models import User

admin.site.register(Posts)
admin.site.register(User)