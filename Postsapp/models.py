from django.db import models

class Majors(models.Model):
    # id	int(11)	    not null	auto_increment	primary key
    name=models.CharField(max_length=20,null=True, default='')	
    
    def __str__(self):
        return self.name
    
class Posts(models.Model):
# id	int(11)	not null	auto_increment	primary key
# major_id	int(11)	not null		foreign key
    major_id=models.ForeignKey("Majors", related_name="fk_post_majors", 
                               on_delete=models.CASCADE, db_column="major_id")
# user_id	int(11)	not null		foreign key
    user_id=models.ForeignKey("Authapp.User", related_name="fk_post_writer", 
                              on_delete=models.CASCADE, db_column="user_id")
# title	varchar(100)	null
    title=models.TextField()
# description	text	not null
    description=models.TextField()
# created_time	datetime	not null
    created_time=models.DateTimeField(auto_now_add=True)
# post_point	int	not null
    post_point=models.IntegerField()
# is_selected	boolean	not null
    is_selcted=models.BooleanField(default=False)
# is_anony	boolean	not null	
    is_anony=models.BooleanField(default=True)
# show_nickname	varchar(100)	not null		
    show_nickname=models.CharField(max_length=20)

