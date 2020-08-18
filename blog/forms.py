from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from blog.models import *
from django.contrib.auth.models import User



class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
