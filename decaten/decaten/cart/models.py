from django.db import models
from catalog_product.models import Product, Flavour

# Create your models here.
class Cart(models.Model):
    sessionkey = models.CharField(max_length=255)
    
class ProductInCart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    count=models.IntegerField()
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE, blank=True, null=True)