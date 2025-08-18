from django.db import models.py

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('starter', "Starter"),
        ("main", 'Main Course'),
        ('dessert', 'Desert'),
        ('drink', 'Drink'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank = True, null=True)
    price = models.DecimalField(max_digit=6, decimal_palces=2)
    catogery = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='main')
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}- ${self.price}"