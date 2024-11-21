from django import forms
from .models import Article
from django.forms.widgets import NumberInput

class ArticleFrom(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__' 
        

class BlogForm(forms.Form):
    name = forms.CharField()
    comment1 = forms.CharField(widget=forms.Textarea)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))