from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import system_admin_required, sales_rep_required
from django.contrib import messages
from . models import Brand, Product
from . forms import BrandCreationForm, ProductCreationForm

# Create your views here.
@login_required
@system_admin_required
def AdminDashboard(request):
    brands =  Brand.objects.all()

    context = {
        'brands': brands,
    }
    return render(request, 'my_shop/systmAdmin/dashboard.html', context)

@login_required
@sales_rep_required
def SalesRepDashboard(request):
    return render(request, 'my_shop/salesRep/dashboard.html')

def brandList(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, 'my_shop/systmAdmin/brand_list.html', context)

@login_required
@system_admin_required
def createBrand(request):
    if request.method == 'POST':
        form = BrandCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Brand Created Successfully')
            return redirect('brand_list')
        else:
            # This runs when form.is_valid() is False
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BrandCreationForm()      
    context = {
        'form' : form,
    }
    return render(request, 'my_shop/systmAdmin/createBrand.html', context)

@login_required
@system_admin_required
def editBrand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        form = BrandCreationForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Brand Updated Successfully')
            return redirect('brand_list')
        else:
            # This runs when form.is_valid() is False
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BrandCreationForm(instance=brand)
    context = {
        'form': form,
    }
    return render(request, 'my_shop/systmAdmin/editBrand.html', context)

def deleteBrand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    brand.delete()
    messages.success(request, 'Brand Deleted Successfully')
    return redirect('brand_list')