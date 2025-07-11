from django.urls import path
from . import views

urlpatterns = [
    path('userRegistration/', views.registerSalesRep, name="userRegistration"),
    path('userLogin/', views.userLogin, name="userLogin"),
    path('logout/', views.userLogout, name='userLogout'),
]
