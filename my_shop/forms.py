from django import forms
from . models import Brand, Product


class BrandCreationForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'logo']

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =  ['name', 'brand', 'description', 'size', 'price', 'quantity_in_stock']
