from django.shortcuts import render, redirect
from cart.cart import Cart
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.


def send(**kwargs):
    
    subject = "Thanks for your order!"
    
    message = render_to_string('email/email_order.html', {
        
        'order': kwargs.get("order"),
        'order_line': kwargs.get('order_line'),
        'username': kwargs.get('user_name'),
        'email': kwargs.get('email')
        
    })
    
    msg = strip_tags(message)
    from_email = "yanmarcoblanvo@gmail.com"
    to = kwargs.get('email')
    
    send_mail(subject, msg, from_email, {to}, html_message=message)
    


@login_required(login_url='/authenticator/login')
def Order_processor(request):
    
    order = models.Orders.objects.create(user=request.user)
    cart = Cart(request)
    order_line = list()
    
    for key, value in cart.cart.items():
        
        order_line.append(models.Order_line(
            
            product_id=key,
            quantity=value['quantity'],
            user=request.user,
            order=order
            
        ))
        
    models.Order_line.objects.bulk_create(order_line)
    
    
    send(
        
        order=order,
        order_line=order_line,
        user_name=request.user.username,
        email=request.user.email
        
    )
    
    
    messages.success(request, 'Order Done!')
    
    return redirect('Home')