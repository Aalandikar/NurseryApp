from django.contrib import admin
from .models import product

# Register your models here.


class product_admin(admin.ModelAdmin):
    list_display=['id','name','price','pdetails','cat','is_active']
    list_filter=['price','cat','is_active']

admin.site.register(product,product_admin)