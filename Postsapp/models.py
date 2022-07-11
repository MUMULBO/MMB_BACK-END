from django.db import models


class Majors(models.Model):
    # id	int(11)	    not null	auto_increment	primary key
    name=models.CharField(max_length=20,null=True, default='')	

class Posts(models.Model):
    #foreignkey
    major_id=models.ForeignKey("Majors", related_name="majors", 
on_delete=models.CASCADE, db_column="major_id", null=True)
    user_id=models.ForeignKey("Authapp.User", related_name="users", 
on_delete=models.CASCADE, db_column="user_id", null=True)
    #userfield
    title=models.TextField()
    description=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    post_point=models.IntegerField()
    is_selcted=models.BooleanField(default=False)
    is_anony=models.BooleanField(default=True)	
    show_nickname=models.CharField(max_length=20, null=True)
    image_src=models.CharField(max_length=30, null=True)
    token=models.CharField(max_length=30, null=True)
    
class Comments(models.Model):
    post_id = models.ForeignKey("Postsapp.Posts", related_name="fk_comment_post", 
                            on_delete=models.CASCADE, db_column="post_id", null=True)
    user_id = models.ForeignKey("Authapp.User", related_name="fk_comment_user",
                                on_delete=models.CASCADE, db_column="user_id",null=True)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    is_selected = models.BooleanField(default=False)
    is_anony = models.BooleanField(default=False)
    token=models.CharField(max_length=30, null=True)
