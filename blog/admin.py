from django.contrib import admin
from blog import models


# Register your models here.


class Post_permit(admin.ModelAdmin):
    
    readonly_fields = ('post_creation','post_update')
    
    
class Category_permit(admin.ModelAdmin):
    
    readonly_fields = ('category_creation','category_date_update')
    
    

admin.site.register(models.Post, Post_permit)
admin.site.register(models.Category, Category_permit)