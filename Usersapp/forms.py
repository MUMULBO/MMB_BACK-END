from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=("email","password")
        
class CreateUserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    checkpassword=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=("email", "password", "nickname")        