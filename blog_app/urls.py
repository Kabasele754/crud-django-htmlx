from django.urls import path, include
from blog_app import views

urlpatterns = [
    path('', views.index),
    path('blogs', views.blog_list, name='blog_list'),
    path('blogs/add', views.add_movie, name='add_blog'),
    path('blogs/<int:pk>/remove', views.remove_blog, name='remove_blog'),
    path('blogs/<int:pk>/edit', views.edit_blog, name='edit_blog'),
]
