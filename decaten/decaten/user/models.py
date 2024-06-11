from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInfo(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)

class MyUser(User):
    number = models.IntegerField()