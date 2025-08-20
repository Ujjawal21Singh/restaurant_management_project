from django import forms
from core.models import MenuItem

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('name', 'image')