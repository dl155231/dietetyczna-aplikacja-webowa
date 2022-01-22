"""Accounts models."""
# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project
from diet_app.models import UserDetails


class CustomUser(AbstractUser):  # noqa: D101
    """Custom User class."""

    user_details = models.ForeignKey(
        UserDetails,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Szczegóły użytkownika'),
    )
