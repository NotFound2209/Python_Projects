from django.db import models


# Create your models here.


class Services(models.Model):
    
    
    title = models.CharField(max_length=120, blank=False, null=False)
    content = models.CharField(max_length=150, blank=False, null=False)
    img = models.ImageField(upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    datetime = models.DateTimeField(verbose_name='Update Date', auto_now=True)
    
    class Meta:
        
        verbose_name = 'service'
        verbose_name_plural = 'services'
        
        def __str__(self) -> str:
            
            return self.title