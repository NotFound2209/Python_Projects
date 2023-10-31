from django.urls import path
from . import views


#//////////////////////////////////////////////////////////


urlpatterns= [
    
    path('', views.Order_processor, name='orders'),
    
]