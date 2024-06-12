from django.db import models

# Create your models here.

class NameOfFilter(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Filter(models.Model):
    name = models.CharField(max_length=255)
    name_of_filter = models.ForeignKey(NameOfFilter, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    filters = models.ManyToManyField(Filter, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Flavour(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.name