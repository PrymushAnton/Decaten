from django.db import models

# Create your models here.
class Carusel(models.Model):
    img = models.ImageField()