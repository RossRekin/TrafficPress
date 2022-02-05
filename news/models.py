import uuid
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Article(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=300)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(
        Category, related_name='categories', blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default='default-article-img.png')
    author = models.ForeignKey(
        User, null=True, blank=False, on_delete=models.SET_NULL)
    #

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
