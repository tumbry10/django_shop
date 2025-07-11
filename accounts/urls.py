from django.urls import path
from . import views

urlpatterns = [
    path('shop_dashboard/', views.SalesRepDashboard, name='salesRepDashboard'),
    path('systad/dashboard/', views.AdminDashboard, name='admindashboard'),
    path('userRegistration/', views.registerSalesRep, name="userRegistration"),
    path('userLogin/', views.userLogin, name="userLogin"),
]
