from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from math import ceil

# Create your views here.

def index(request):
    # products = Product.objects.all()

    # n = len(products)  # length of products
    # nSlides = n//4 + ceil((n/4)-(n//4))   # Number of slides

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)  # length of products
        nSlides = n//4 + ceil((n/4)-(n//4))   # Number of slides
        allProds.append([prod, range(1, nSlides), nSlides])
    # context = {'products':products, 'no_of_slides':nSlides, 'range':range(1, nSlides)}
    # all_products = [
    #     [products, range(1, nSlides), nSlides],
    #     [products, range(1, nSlides), nSlides]
    # ]

    context = {'all_products':allProds}
    return render(request, 'shop/index.html', context)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at productView")

def checkout(request):
    return HttpResponse("We are at checkout")
