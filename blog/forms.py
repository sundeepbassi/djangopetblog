"""This module specifies all of our forms code"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """This class specifies the comment form"""
    class Meta:
        """This class specifies the comment body"""
        model = Comment
        fields = ('body',)
