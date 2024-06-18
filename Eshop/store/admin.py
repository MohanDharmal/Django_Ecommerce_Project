from django.contrib import admin
from store.models.Product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order


# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)