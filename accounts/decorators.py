from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def system_admin_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 1:
            return view_func(request, *args, **kwargs)
        else:
            #raise PermissionDenied  # or redirect somewhere else if you prefer
            return redirect('salesRepDashboard')
    return wrapper_func


def sales_rep_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 2:
            return view_func(request, *args, **kwargs)
        else:
            #raise PermissionDenied  # or redirect somewhere else
            return redirect('admindashboard')
    return wrapper_func