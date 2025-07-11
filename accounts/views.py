from django.shortcuts import render, redirect
from .forms import SalesRepRegForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerSalesRep(request):
    if request.method == 'POST':
        form = SalesRepRegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sales Representative Registered Successfully')
            return redirect('userLogin')
    else:
        form = SalesRepRegForm()
    context = {'form': form}
    return render(request, 'accounts/UserRegister.html', context)
    
def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                # Role-based redirection
                if user.user_type == 1:  # SystemAdmin
                    return redirect('admindashboard')
                elif user.user_type == 2:  # SalesRep
                    return redirect('salesRepDashboard')
                else:
                    # fallback if for some reason user_type is invalid
                    messages.error(request, 'Invalid user type.')
                    return redirect('userLogin')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/userLogin.html', {'form': form})

@login_required
def AdminDashboard(request):
    return render(request, 'accounts/systmAdmin/dashboard.html')

@login_required
def SalesRepDashboard(request):
    return render(request, 'accounts/salesRep/dashboard.html')