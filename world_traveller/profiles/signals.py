from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from world_traveller.profiles.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    """A signal that shows if a user created a specific place."""
    if created:
        profile = Profile(
            user=instance,
        )
        profile.save()


@receiver(pre_save, sender=Profile)
def check_is_complete(sender, instance, **kwargs):
    """
    A signal that shows if a user's profile is totally
    completed. Once all profile fields are filled,
    the message for incomplete profile does not show anymore.
    """
    if instance.first_name and instance.last_name and instance.age and instance.about_me:
        instance.is_complete = True
