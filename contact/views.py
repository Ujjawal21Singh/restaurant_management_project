from django.shortcuts import render, redirect
from .form import ContactForm

def cntactView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.clean_data['name']
            email = form.clean_data['email']
            message = form.clean_data['message']

        elese:
        form=ContactForm()
    return render(request, 'contact.html', {"form":form})