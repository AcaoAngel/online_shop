from django import forms
from .models import Products

class Products_form(forms.ModelForm):
    name=forms.CharField(max_length=100)
    description=forms.CharField(max_length=500, widget=forms.Textarea)
    price=forms.DecimalField(max_digits=11, decimal_places=2)
    picture=forms.ImageField()

    class Meta():
        model = Products
        fields = ["name", "description", "price", "picture"]