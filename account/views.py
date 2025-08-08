from django.shortcuts import render

# Create your views here.
from .models import RestaurantInfo

def home(request):
    restaurant = RestaurantInfo.objects.first()
    context = {
        'phone_number': restaurant.phone_number if restaurant else None
    }
    resturm render(request, 'home.html', context)