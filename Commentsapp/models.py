from django.db import models

class Comments(models.Model):
    #id
    post_id = models.ForeignKey("Postsapp.Posts", related_name="fk_comment_post", 
                               on_delete=models.CASCADE, db_column="post_id")
    user_id = models.ForeignKey("Authapp.User", related_name="fk_comment_user",
                                on_delete=models.CASCADE, db_column="user_id")
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    is_selected = models.BooleanField(default=False)
    is_anony = models.BooleanField(default=False)