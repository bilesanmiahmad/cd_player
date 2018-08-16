from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['slug', 'author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
