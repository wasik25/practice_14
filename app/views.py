from django.shortcuts import render
from .forms import ArticleFrom,BlogForm
# Create your views here.
def home(request):
    article_form  = ArticleFrom()
    blog_form  = BlogForm()
    return render(request, 'base.html', {'form': article_form,'blog': blog_form })

def blog(request):
    blog_form  = BlogForm()
    return render(request, 'base.html', {'blog': blog_form })

