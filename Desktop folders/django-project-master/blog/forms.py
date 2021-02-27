from django import forms 
from .models import Post, Comment
  
class Postimage(forms.ModelForm): 
  
    class Meta: 
        model = Post
        fields = ['title', 'content'] 

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)