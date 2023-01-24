from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """ Form to create a Post obj """
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category',

        ]


class CommentForm(forms.ModelForm):
    """ Form to create a Comment obj """
    class Meta:
        model = Comment

        fields = [
            'text',

        ]
