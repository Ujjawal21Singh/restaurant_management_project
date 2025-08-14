from django,shortcuts import render
from .models import MenuItem

def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu_item.html', {"menu_item": items})