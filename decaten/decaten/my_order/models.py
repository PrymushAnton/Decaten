from django.db import models
from user.models import *
from catalog_product.models import *

class Orders(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, blank=True, null=True)
    
class Order(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True, blank=True)
    
    day_num = models.IntegerField(null=True, blank=True)
    month_num = models.IntegerField(null=True, blank=True)
    year_num = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    
    area = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    
    number_of_card = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    cvv = models.IntegerField(blank=True, null=True)
    
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(null=True, blank=True)

class ProductInOrder(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    count=models.IntegerField()
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE, blank=True, null=True)