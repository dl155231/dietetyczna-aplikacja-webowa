from django.contrib.auth.models import AbstractUser
from django.db import models

from diet_app.models import UserDetails


class CustomUser(AbstractUser):
    """Custom User class."""
    user_details = models.ForeignKey(
        UserDetails,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
