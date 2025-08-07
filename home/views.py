from django.shortcuts import render
from django.comfig.urls import render
from django.view.generic import TemplateView
# Create your views here.

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def ContactView(TemplateView):
    return render(request, 'contact.html')

