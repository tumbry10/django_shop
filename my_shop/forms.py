from django import forms
from . models import Brand, Product, StockInItem, Sale, SaleItem
from django.forms import formset_factory


class BrandCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Enter Brand Name' 
    }))
    logo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
        'accept': 'image/*'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Product Description',
        'rows': 3
    }))
    class Meta:
        model = Brand
        fields = ['name', 'description', 'logo']

class ProductCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Enter Product Name' 
    }))
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), widget=forms.Select(attrs={
            'class': 'form-control text-center',
        }),
        empty_label="-- -Select Product's Brand- --"
    )
    size = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Enter Product Size/Weight (ml/Kgs)' 
    }))
    quantity_in_stock = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Enter Quantity' 
    }))
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.0,
        widget=forms.NumberInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Enter Product Price' 
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Product Description',
        'rows': 3
    }))
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