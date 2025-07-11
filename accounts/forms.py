from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser

class SalesRepRegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    #Overide save method to set user_type
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2  #SalesRep user_type
        print("Setting user_type to SalesRep")
        if commit:
            user.save()
        return user