from django.urls import path
from . import views

urlpatterns = [
    path('shop_dashboard/', views.SalesRepDashboard, name='salesRepDashboard'),
    path('systad_dashboard/', views.AdminDashboard, name='admindashboard'),
    path('brands/create_brand/', views.createBrand, name='create_brand'),
    path('brands/list/', views.brandList, name='brand_list'),
    path('brands/edit/<int:pk>/', views.editBrand, name='edit_brand'),
    path('brands/delete/<int:pk>/', views.deleteBrand, name='delete_brand'),
]
