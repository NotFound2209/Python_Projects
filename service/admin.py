from django.contrib import admin
from service import models


# Register your models here.


class Services_permit(admin.ModelAdmin):
    
    list_display = ('title', 'content', 'img', 'created', 'datetime')
    search_fields = ('title', 'img', 'created')
    date_hierarchy = ('created')
    
    
admin.site.register(models.Services, Services_permit)