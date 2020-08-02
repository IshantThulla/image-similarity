from .models import Post
from django import forms
from django.forms import ModelForm
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ["name", "email", "subject", "message"]