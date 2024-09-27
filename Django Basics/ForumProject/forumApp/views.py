from django.http import HttpResponse
from django.shortcuts import render
from django.utils.text import slugify

from forumApp.models import Post, Articles


# Create your views here.

def index(request):

    article = Articles.get_article_for_url('home')


    context = {
        'article': article,

    }

    return render(request, 'home.html', context)

def dashboard(request):
    posts = Post.get_all_posts()

    context = {
        'posts': posts
    }

    return render(request, 'posts/posts.html', context)

def article(request,**kwargs):
    title = slugify(kwargs['title'])
    article = Articles.get_article_for_url(title)

    context = {
        'article': article
    }

    return render(request, 'articles/article.html', context)

def posts(request,**kwargs):
    pk = kwargs['pk']
    post = Post.get_post_by_id(pk)

    context = {
        'article': post
    }

    return render(request, 'articles/article.html', context)