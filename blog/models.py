from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    
    category_name = models.CharField(max_length=25, verbose_name="Category Name", blank=False, null=False)
    category_creation = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date", blank=False, null=False)
    category_date_update = models.DateTimeField(auto_now=True, verbose_name='Update Date', blank=False, null=False)
    
    
    class Meta:
        
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
        
    def __str__(self) -> str:
        return self.category_name
    
    
class Post(models.Model):
    
    title = models.CharField(max_length=35, blank=False, null=False, verbose_name='Title')
    content = models.CharField(max_length=600, blank=False, null=False, verbose_name='Content')
    img = models.ImageField(verbose_name='Image', upload_to='blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    post_creation = models.DateTimeField(auto_now_add=True, verbose_name='Post Creation')
    post_update = models.DateTimeField(auto_now=True, verbose_name='Post Update')
    
    
    class Meta:
        
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
        
    def __str__(self) -> str:
        return self.title