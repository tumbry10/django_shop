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
    products = Product.objects.all()

    context = {
        'brands': brands,
        'products': products
    }
    return render(request, 'my_shop/systmAdmin/dashboard.html', context)

@login_required
@sales_rep_required
def SalesRepDashboard(request):
    return render(request, 'my_shop/salesRep/dashboard.html')

@login_required
@system_admin_required
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


@login_required
@system_admin_required
def deleteBrand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    brand.delete()
    messages.success(request, 'Brand Deleted Successfully')
    return redirect('brand_list')

@login_required
@system_admin_required
def listProduct(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'my_shop/systmAdmin/product_list.html', context)

@login_required
@system_admin_required
def createProduct(request):
    form = ProductCreationForm()
    if request.method == 'POST':
        form = ProductCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Created Successfully')
            return redirect('list_product')
        else:
            # This runs when form.is_valid() is False
            messages.error(request, 'Please correct the errors below.')
    else:
        # This runs when request.method is 'GET'
        form = ProductCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'my_shop/systmAdmin/createProduct.html', context)

@login_required
@system_admin_required
def editProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductCreationForm(request.POST or None, request.FILES or None, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated Successfully')
            return redirect('list_product')
        else:
            # This runs when form.is_valid() is False
            messages.error(request, 'Please correct the errors below.')
    else:
        # This runs when request.method is 'GET'
        form = ProductCreationForm(instance=product)
    context = {
        'form': form,
    }
    return render(request, 'my_shop/systmAdmin/editProduct.html', context)

@login_required
@system_admin_required
def deleteProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'Product Deleted Successfully')
    return redirect('list_product')