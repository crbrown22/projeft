from django import forms
from .models import Product, Order
from user_app.models import User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'category', 'quantity']
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','order_quantity']