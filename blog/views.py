from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def blogpost(request):
    return render(request, 'blog/blogpost.html')
