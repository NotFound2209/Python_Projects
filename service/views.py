from django.shortcuts import render
from service.models import Services


# Create your views here.


def services(request):
    
    
    srv = Services.objects.all()
    return render(request, 'service/Service.html', {'test':srv})