from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, UserProfile, SystemAdmin, SalesRep
from django.utils.translation import gettext_lazy as _

# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    # Add the user_type field to the admin form
    fieldsets = BaseUserAdmin.fieldsets + (
        (_('User Type & Role'), {'fields': ('user_type',)}),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (_('User Type & Role'), {'fields': ('user_type',)}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(SystemAdmin)
admin.site.register(SalesRep)