from django.contrib import admin
from .models import Product , ProductImage ,Category,Product_Alternative,Product_accessories,Review,ContactUs

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_accessories)
admin.site.register(Review)
admin.site.register(ContactUs)