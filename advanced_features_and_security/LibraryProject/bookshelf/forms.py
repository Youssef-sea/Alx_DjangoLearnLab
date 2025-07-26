
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

# New: ExampleForm for general purpose input

class ExampleForm(forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=100)
    your_email = forms.EmailField(label="Your Email")
    message = forms.CharField(label="Your Message", widget=forms.Textarea)
    newsletter_signup = forms.BooleanField(label="Sign up for newsletter?", required=False)