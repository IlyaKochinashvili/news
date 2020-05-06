from django import forms
from django.forms import ModelForm

from posts.models import Post, Comment


class PostForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ['text']


class CommentForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['text']