from django import forms
from . models import Brand, Product, StockInItem, Sale, SaleItem
from django.forms import formset_factory


class BrandCreationForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'logo']

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =  ['name', 'brand', 'description', 'size', 'price', 'quantity_in_stock']

class StockInItemForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Product')
    quantity_received = forms.IntegerField(min_value=1, label='Quantity Received')

StockInItemFormSet = formset_factory(StockInItemForm, extra=1)  # start with 1 item in the formset

class SaleItemForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Product')
    quantity_sold = forms.IntegerField(min_value=1, label='Quantity Sold')

SaleItemFormSet = formset_factory(SaleItemForm, extra=1)  # start with 1 item in the formset