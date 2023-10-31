from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField
from shop.models import Product_details



# Create your models here.


User = get_user_model()


class Orders(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        
        return self.id
    
    
    @property
    def total(self):
        
        return self.Order_line_set.aggregate(
            
            total = Sum(F("product_price")*F("product_price"), output_field=FloatField())
            
            
        )['total']
    
    
    class Meta:
        
        db_table = 'Orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['id']
        
        
        
class Order_line(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product_details, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        
        return f'{self.quantity} units of {self.product.product_name}'
    
    
    class Meta:
        
        db_table = 'Order Line'
        verbose_name = 'Order line'
        verbose_name_plural = 'Order line'
        ordering = ['id']