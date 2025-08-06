from django.shortcuts import render
from django.config import settings
# Create your views here.
 def homepage(request):
    restaurant_name= settings.restaurant_name
    return render(request, 'homepage.html', {'restaurant_name': restaurant_name})
    