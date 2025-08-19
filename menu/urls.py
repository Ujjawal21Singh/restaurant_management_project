from django.urls import path
from . import views
from restaurant_management import settings
urlpatterns = [
    path('', views.menu_list, name='menu_list'),
]+ static(setting.MEDIA_URL, document_root=settings.MEDIA_ROOT)