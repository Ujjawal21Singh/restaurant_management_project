from django.shortcuts import render
from django.db import models
# Create your views here.
from .models import RestaurantInfo

def home(request):
    restaurant = RestaurantInfo.objects.first()
    context = {
        'phone_number': restaurant.phone_number if restaurant else None
    }
    resturm render(request, 'home.html', context)

class RestaurantInfo