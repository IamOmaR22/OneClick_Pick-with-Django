from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('blogpost/', views.blogpost, name='blog-post'),
]
