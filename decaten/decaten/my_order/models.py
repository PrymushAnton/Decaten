from django.db import models
from user.models import *
from catalog_product.models import *

# Create your models here.
# class Order(models.Model):
#     area = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
    
#     payment_by_card = models.BooleanField()
    
#     number_of_card = models.IntegerField(null=True, blank=True)
#     month = models.IntegerField(null=True, blank=True)
#     year = models.IntegerField(null=True, blank=True)
#     cvv = models.IntegerField(null=True, blank=True)
    
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     middle_name = models.CharField(max_length=255)
#     phone_number = models.IntegerField()

class Orders(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, blank=True, null=True)
    
class Order(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True, blank=True)
    
    # date = models.DateField(null=True, blank=True)
    day_num = models.IntegerField(null=True, blank=True)
    month_num = models.IntegerField(null=True, blank=True)
    year_num = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    
    area = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

class ProductInOrder(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    count=models.IntegerField()
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE, blank=True, null=True)