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
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    filters = models.ManyToManyField(Filter)

    
    def __str__(self):
        return self.name
    

class Flavour(models.Model):
    name = models.CharField(max_length=255)
    for_product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    count_of_product = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name
    



