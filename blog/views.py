from django.shortcuts import render
from blog import models


# Create your views here.


def blog(request):
    
    
    post = models.Post.objects.all()
    
    return render(request, 'blog/Blog.html', {'post':post})


def category(request, category_id):
    
    
    categories = models.Category.objects.get(id = category_id)
    post = models.Post.objects.filter(category = categories)
    
    return render(request, 'blog/Category.html', {'category':categories, 'post':post})