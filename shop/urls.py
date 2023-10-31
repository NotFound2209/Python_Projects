from django.urls import path
from . import views


#//////////////////////////////////////////////////////


urlpatterns = [
    
    path('', views.shop, name='Shop'),
    path('filter/<int:category_id>/', views.filter, name='Filter'),
    path('auth/', views.auth, name='Auth'),
    path('cart/', views.cart, name='Cart'),
]