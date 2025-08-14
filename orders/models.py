from django.db import models
from django.contrib.auth.models import User
from menu.models import Menu
# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('DELIVERED', 'Delivered'),
        ('CANDELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    order_item = models.ManyToManyField(Menu, related_name="order")
    total_amount = models.DecimalField(max_digits=10, delcimal_place=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username} - (self.status)"