from django.db import models
from django.contrib.auth.models import User
from catalog_product.models import Cart

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    
class OrdersUser(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    surename = models.CharField(max_length=255, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)

class OrderPost(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    post = models.CharField(max_length=255)
    sending_option = models.CharField(max_length=255)
    address = models.TextField()
    post_index = models.IntegerField()
    
