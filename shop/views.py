from django.shortcuts import render, redirect
from . import models


# Create your views here.


def shop(request):
    
    
    products = models.Product_details.objects.all()
    
    return render(request, 'shop/Shop.html', {'products':products})


def filter(request, category_id):
    
    categories = models.Category.objects.get(id = category_id)
    product_filter = models.Product_details.objects.filter(product_category = categories)
    
    return render(request, 'shop/Category.html', {'categories':categories, 'product_filter':product_filter})


def auth(request):
    
    return render(request, 'shop/auth.html')


def cart(request):
    
    return render(request, 'cart/cart.html')