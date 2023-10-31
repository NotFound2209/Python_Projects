from django.urls import path
from .views import View_register
from . import views


#////////////////////////////////////////


urlpatterns = [
    
    path('', View_register.as_view(), name='authenticator'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
]