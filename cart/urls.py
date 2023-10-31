from django.urls import path
from . import views


#///////////////////////////////////////////


app_name = "cart"


urlpatterns = [
    
    path("add/<int:product_id>/", views.add_product_to_the_cart, name="add"),
    path("delete/<int:product_id>/", views.delete_product_to_the_cart, name="delete"),
    path("subtract/<int:product_id>/", views.subtract_product, name="subtract"),
    path("clear/", views.clear_the_cart, name="clear")
    
]