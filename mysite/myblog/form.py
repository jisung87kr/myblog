from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('autor', 'title', 'content', 'files', 'created_date', 'published_date')
