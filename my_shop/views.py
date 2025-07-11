from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import system_admin_required, sales_rep_required

# Create your views here.
@login_required
@system_admin_required
def AdminDashboard(request):
    return render(request, 'my_shop/systmAdmin/dashboard.html')

@login_required
@sales_rep_required
def SalesRepDashboard(request):
    return render(request, 'my_shop/salesRep/dashboard.html')