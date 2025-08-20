from django,shortcuts import render
from .models import MenuItem
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import MenuForm

def MenuAPIView(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        context = {'form':MenuForm()}
        menu = [
            {
                "name": item.name,
                "description": item.description
                "price": item.price
            }
            for item in menu_items
        ]
        return Response(request, "menu.html", context)