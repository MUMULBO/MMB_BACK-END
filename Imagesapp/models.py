from django.db import models

class Images(models.Model):
    #id
    src = models.CharField(max_length=100)
    
    post_id = models.ForeignKey("Postsapp.Posts", related_name="fk_image_post",
                                on_delete=models.CASCADE, db_column="post_id")
    
    order = models.IntegerField()