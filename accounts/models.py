from django.contrib.auth.models import AbstractUser
from django.db import models

# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_choices = (
        (1, "SystAdmin"),
        (2, "SalesReps")
    )
    user_type = models.PositiveSmallIntegerField(default=1, choices=user_type_choices, max_length=20)

    class Meta:
        db_table = "custom_user"

        
    def __str__(self):
        return self.username

class SystemAdmin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'system_admin'

    def __str__(self):
        return f"SystemAdmin: {self.user.username}"


class SalesRep(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sales_rep'

    def __str__(self):
        return f"SalesRep: {self.user.username}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    class Meta:
        db_table = 'user_rofile'

    def __str__(self):
        return f"{self.user.username}'s Profile"
