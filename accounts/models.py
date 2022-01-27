"""Accounts models."""
# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# 3rd-party
from diet_app.models import Nutritionist
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

    is_nutritionist = models.BooleanField(_('Czy dietetyk'), default=False)
    nutritionist = models.OneToOneField(
        Nutritionist,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Dietetyk'),
    )

    def __str__(self):  # noqa: D105
        return self.get_full_name()
