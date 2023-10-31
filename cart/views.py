from django.shortcuts import render, redirect
from .cart import Cart
from shop.models import Product_details


# Create your views here.


def add_product_to_the_cart(request, product_id):
    
    
    shopping_cart = Cart(request)
    
    prod = Product_details.objects.get(id = product_id)
    
    shopping_cart.add_product(prod)
    
    
    return redirect('Cart')


def delete_product_to_the_cart(request, product_id):
    
    
    shopping_cart = Cart(request)
    
    prod = Product_details.objects.get(id = product_id)
    
    shopping_cart.delete_product(prod)
    
    
    return redirect('Cart')


def subtract_product(request, product_id):
    
    
    shopping_cart = Cart(request)
    
    prod = Product_details.objects.get(id = product_id)
    
    shopping_cart.subtract_product(prod)
    
    
    return redirect('Cart')


def clear_the_cart(request):
    
    
    shopping_cart = Cart(request)
    
    shopping_cart.clear_cart()
    
    
    return redirect('Cart')