from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, UserProfile, SystemAdmin, SalesRep

@receiver(post_save, sender=CustomUser)
def create_user_related_profiles(sender, instance, created, **kwargs):
    if created:
        # Create UserProfile for every user
        UserProfile.objects.create(user=instance)

        # Create SystemAdmin or SalesRep based on user_type
        if instance.user_type == 1:  # SystemAdmin
            SystemAdmin.objects.create(user=instance)
        elif instance.user_type == 2:  # SalesRep
            SalesRep.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    # Ensure profile always saves when user saves
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
