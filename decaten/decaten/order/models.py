from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Orders(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    surename = models.CharField(max_length=255, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    