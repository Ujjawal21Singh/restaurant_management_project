from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(USer, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(Self):
        return self.name
