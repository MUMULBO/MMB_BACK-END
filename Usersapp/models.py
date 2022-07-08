from platform import release
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        user=self.model(
            email=email,
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, nickname, password):
        u=self.create_user(email=email,
                           nickname=nickname,
                           password=password,
                    )
        u.is_admin=True
        u.save(using=self._db)
        return u
        
    
    
class User(AbstractBaseUser):
    group_id=models.IntegerField()
    nickname=models.CharField(max_length=20, default='',unique=True)
    email=models.CharField(max_length=20, unique=True)    
    point=models.IntegerField()
    major_id=models.ForeignKey("Postsapp.Majors", related_name="majors_id", on_delete=models.CASCADE, db_column="major_id")
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
