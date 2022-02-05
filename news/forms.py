from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'featured_image', 'categories', ]
