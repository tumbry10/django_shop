from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import system_admin_required, sales_rep_required
from django.contrib import messages
from . models import Brand, Product, StockIn, StockInItem, Sale, SaleItem
from . forms import BrandCreationForm, ProductCreationForm, StockInItemFormSet, SaleItemFormSet
from accounts.models import CustomUser
from django.db.models import F

# Create your views here.
@login_required
@system_admin_required
def AdminDashboard(request):
    brands =  Brand.objects.all()
    products = Product.objects.all()

    total_brands = Brand.objects.count()
    total_products = Product.objects.count()
    total_stock_in = StockIn.objects.count()
    total_sales =  Sale.objects.count()
    total_sales_reps = CustomUser.objects.filter(user_type=2).count()
    total_admins = CustomUser.objects.filter(user_type = 1).count()
    total_users = CustomUser.objects.count()

    low_stock_products = Product.objects.filter(quantity_in_stock__lte=F('low_stock_threshold')).order_by('quantity_in_stock')


    context = {
        'brands': brands,
        'products': products,
        'total_brands': total_brands,
        'total_products': total_products,
        'total_stock_in': total_stock_in,
        'total_sales': total_sales,
        'total_sales_reps': total_sales_reps,
        'total_admins': total_admins,
        'total_users': total_users,
        'low_stock_products': low_stock_products
    }
    return render(request, 'my_shop/systmAdmin/dashboard.html', context)

@login_required
@sales_rep_required
def SalesRepDashboard(request):
    total_my_sales = Sale.objects.filter(sold_by = request.user).count()
    total_my_stock_in = StockIn.objects.filter(received_by = request.user).count()
    total_products_available = Product.objects.count()
    latest_sales = Sale.objects.filter(sold_by = request.user).order_by('-date_sold')[:5] #Show last 5 sales made by the sales rep
    low_stock_products = Product.objects.filter(quantity_in_stock__lte=F('low_stock_threshold')).order_by('quantity_in_stock')


    context = {
        'total_my_sales': total_my_sales,
        'total_my_stock_in': total_my_stock_in,
        'total_products_available' : total_products_available,
        'latest_sales' : latest_sales,
        'low_stock_products' : low_stock_products
    }
    return render(request, 'my_shop/salesRep/dashboard.html', context)

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

@login_required
@sales_rep_required
def receiveStock(request):
    if request.method == 'POST':
        formset = StockInItemFormSet(request.POST)

        if formset.is_valid():
            # Create StockIn record (auto date, sets received_by)
            stockIn = StockIn.objects.create(received_by=request.user)

            for form in formset:
                if form.cleaned_data and form.cleaned_data.get('product') and form.cleaned_data.get('quantity_received'):
                    product = form.cleaned_data['product']
                    quantity_received = form.cleaned_data['quantity_received']

                    # Create StockInItem
                    StockInItem.objects.create(
                        stock_in=stockIn,
                        product=product,
                        quantity_received=quantity_received
                    )

                    # Update product quantity
                    product.quantity_in_stock += quantity_received
                    product.save()

            messages.success(request, 'Stock Received Successfully')
            return redirect('salesRepDashboard')
        else:
            # This runs when formset.is_valid() is False
            messages.error(request, 'Please correct the errors below.')
    else:
        formset = StockInItemFormSet()
    
    context = {
        'formset': formset,
    }
    return render(request, 'my_shop/salesRep/receiveStock.html', context)

@login_required
def stockInReceipt(request, pk):
    stock_in = get_object_or_404(StockIn, pk=pk)
    print(stock_in)
    items = StockInItem.objects.filter(stock_in=stock_in) #filtering items of the specific stockIn

    total_quantity = sum(item.quantity_received for item in items)

    context = {
        'stock_in': stock_in,
        'items': items,
        'total_quantity': total_quantity,
    }
    return render(request, 'my_shop/stockInReceipt.html', context)

@login_required
@sales_rep_required
def makeSale(request):
    if request.method == 'POST':
        formset = SaleItemFormSet(request.POST)
        if formset.is_valid():
            sale = Sale.objects.create(sold_by=request.user)
            total_amount = 0
            for form in formset:
                if form.cleaned_data:
                    product = form.cleaned_data['product']
                    quantity_sold = form.cleaned_data['quantity_sold']

                    if product.quantity_in_stock < quantity_sold:
                        messages.error(request, f"Not enough stock for {product.name}. Available: {product.quantity_in_stock}")
                        sale.delete() #rollback sale
                        return redirect('makeSale')
                    
                    price_at_sale = product.price
                    line_total = price_at_sale * quantity_sold
                    total_amount += line_total

                    #create sale item
                    SaleItem.objects.create(
                        sale =sale,
                        product = product,
                        quantity_sold = quantity_sold,
                        price_at_sale = price_at_sale
                    )
                    #Update stock details
                    product.quantity_in_stock -= quantity_sold
                    product.save()
            sale.total_amount = total_amount
            sale.save()

            messages.success(request, 'Sale Completed Successfully')
            return redirect('salesRepDashboard')
        else:
            # This runs when form.is_valid() is False            
            messages.error(request, 'Invalid Form Data')
    else:
        formset = SaleItemFormSet()
    context = {
        'formset': formset,
    }
    return render(request, 'my_shop/salesRep/makeSale.html', context)

@login_required
def saleInvoice(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    items = sale.items.all() #get all sale items for this sale, thanks to related_name='items'

    context = {
        'sale': sale,
        'items': items,
    }
    return render(request, 'my_shop/saleInvoice.html', context)