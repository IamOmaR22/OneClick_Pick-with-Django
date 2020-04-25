from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop-home'),
    path('about/', views.about, name='about-me'),
    path('contact/', views.contact, name='contact-me'),
    path('tracker/', views.tracker, name='tracking-status'),  # using tracking id, i can know the order status
    path('search/', views.search, name='search'),
    path('product_view/', views.productView, name='product-view'),  # after Click on a prooduct can see the details
    path('checkout/', views.checkout, name='checkout'),
]
