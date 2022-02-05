from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Category, Article
from .utils import filter_articles_by_category
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def news(request):
    categories = Category.objects.all()
    articles, categeory_query = filter_articles_by_category(request)
    articles = articles.order_by('-created')
    context = {'categories': categories, 'articles': articles,
               'categeory_query': categeory_query}
    return render(request, 'news/news.html', context)


def article(request, pk):
    article = Article.objects.get(id=pk)
    categories = Category.objects.all()
    context = {'article': article, 'categories': categories}
    return render(request, 'news/article.html', context)


@login_required(login_url='/login')
def create_article(request):
    user = request.user
    print(user)
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid:
            article = form.save(commit=False)
            article.author = user
            form.save()
            return redirect('news')
    context = {'form': form}
    return render(request, 'news/article_form.html', context)


@login_required(login_url='/login')
def delete_article(request, pk):
    article = Article.objects.get(id=pk)
    if request.user != article.author:
        return redirect('news')
    if request.method == 'POST':
        article.delete()
        return redirect('news')
    context = {'object': article}
    return render(request, 'delete_template.html', context)


@login_required(login_url='/login')
def update_article(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)
    if request.user != article.author:
        return redirect('news')
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid:
            form.save()
            return redirect('news')

    context = {'form': form}
    return render(request, 'news/article_form.html', context)
