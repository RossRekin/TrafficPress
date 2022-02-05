from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name="news"),
    path('article/<str:pk>', views.article, name="single-article"),
    path('create-article/', views.create_article, name="create-article"),
    path('delete-article/<str:pk>/', views.delete_article, name="delete-article"),
    path('update-article/<str:pk>/', views.update_article, name="update-article"),


]
