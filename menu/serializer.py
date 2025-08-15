from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        models = MenuItem
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'available',
            'created_at',
        ]