from django.contrib import admin

# Register your models here.

from .models import Product
# import the Product class

admin.site.register(Product)
