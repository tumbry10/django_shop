from django.urls import path
from . import views

urlpatterns = [
    path('shop_dashboard/', views.SalesRepDashboard, name='salesRepDashboard'),
    path('systad_dashboard/', views.AdminDashboard, name='admindashboard'),
]
