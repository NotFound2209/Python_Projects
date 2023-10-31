


#/////////////////////////////////////////////////


def total_cart(request):
    
    
    total = 0
    
    
    if request.user.is_authenticated:
        
        for key, value in request.session["cart"].items():
            
            total += float(value['price'])
            
    
    return {'total_cart':total}