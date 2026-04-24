from django.contrib import admin

# Register your models here.

from .models import Product, Category
from django.contrib import admin

admin.site.register(Product)
admin.site.register(Category)