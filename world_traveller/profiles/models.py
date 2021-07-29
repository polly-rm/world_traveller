from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
    )
    about_me = models.TextField(
        blank=True,
        null=True,
    )
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    is_complete = models.BooleanField(
        default=False,
    )
