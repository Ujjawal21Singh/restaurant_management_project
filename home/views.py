from django.shortcuts import render
from django.comfig.irls import render
# Create your views here.

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404

