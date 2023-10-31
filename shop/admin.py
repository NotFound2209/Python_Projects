from django.contrib import admin
from . import models


# Register your models here.


class Products_permissions(admin.ModelAdmin):
    
    
    list_display = ('product_name', 'product_details', 'product_img', 'product_stockist', 'product_price', 'product_post_creation', 'product_post_update')
    search_fields = ('product_name',)
    list_filter = ('product_category', 'product_stockist')
    date_hierarchy = ('product_post_update')
    readonly_fields = ('product_post_update', 'product_post_creation')
    
    
class Category_permissions(admin.ModelAdmin):
    
    
    list_display = ('category_name',)
    date_hierarchy = ('category_update')
    readonly_fields = ('category_update', 'category_creation')
    
    
admin.site.register(models.Product_details, Products_permissions)
admin.site.register(models.Category, Category_permissions)