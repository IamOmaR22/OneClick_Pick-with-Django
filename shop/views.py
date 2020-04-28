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
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, pid):
    # Fetch the product using the id
    product = Product.objects.filter(id=pid)

    return render(request, 'shop/prod_view.html', {'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')
