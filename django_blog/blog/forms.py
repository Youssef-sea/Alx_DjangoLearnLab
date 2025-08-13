# blog/forms.py
from django import forms
from .models import Post, Comment

class TagWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        attrs = {'class': 'tag-input'}
        super().__init__(attrs=attrs, *args, **kwargs)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }
    pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']