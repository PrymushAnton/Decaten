from django.contrib import admin
from .models import Product, NameOfFilter, Filter, Flavour

# Register your models here.
admin.site.register(Product)
admin.site.register(NameOfFilter)
admin.site.register(Filter)
admin.site.register(Flavour)
