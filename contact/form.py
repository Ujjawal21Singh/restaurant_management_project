from django import forms
from django.core.mail import send_mail

send_mail(
    'Subject',
    "write message",
    'from@example.com',
    ['restaurant@restaurant.com'],
    fail_silently=False
)


class ContactForm(form.Form):
    name = form.CharField(max_length=100, label="Your name")
    email = send_mail
    