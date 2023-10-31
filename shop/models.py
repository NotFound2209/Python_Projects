from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    
    category_name = models.CharField(max_length=75, verbose_name='Name', blank=False, null=False)
    category_creation = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    category_update = models.DateTimeField(auto_now=True, verbose_name='Update date')
    
    
    class Meta:
        
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
        
    def __str__(self) -> str:
        return self.category_name
    
    
    
class Product_details(models.Model):
    
    product_name = models.CharField(max_length=50, verbose_name='Product Name', blank=False, null=False)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)   
    product_details = models.CharField(max_length=500, verbose_name='Description')
    product_img = models.ImageField(verbose_name='Product Image', upload_to='shop', null=True, blank=True)
    product_post_creation = models.DateTimeField(auto_now_add=True, verbose_name='Post Created')
    product_post_update = models.DateTimeField(auto_now=True, verbose_name='Post Update')
    product_stockist = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_price = models.FloatField(verbose_name='Product Price', null=True, blank=True)
    product_disponibilidad = models.BooleanField(default=True)
    
    
    class Meta:
        
        verbose_name = 'Product Detail'
        verbose_name_plural = 'Products Details'
        
        
    def __str__(self) -> str:
        return self.product_name
    
    