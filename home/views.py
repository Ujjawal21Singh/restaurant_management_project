from django.shortcuts import render
from django.comfig.urls import render
from django.view.generic import TemplateView
from .models import Reservation
from django.db import DatabaseError 
import requests
from restaurant_management import settings
# Create your views here.

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def ContactView(TemplateView):
    return render(request, 'contact.html')

def reservations_view(request):
    try:
        reservations = Reservation.objects.all()
        return render(request, "reservations.html", {"reservations": reservations})

    except DatabaseError as e:
        return HttpResponse("Sorry, we are experiencing technical issues.", status=500)
    
    except Exception as e:
        return HttpResponse("An unexpected error occured", status=500)

def home(request):
    try:
        response = request.get("http://127.0.0.1:800/api/menu")
        menu_item = response.json() if response.status_code == 200 else []
    except Exception:
        menu_item=[]
    
    context = {
        "reservation_name": settings.RESTAURANT_NAME,
        "menu_item": menu_item,
    }
    return render(request, "homepage.html")

