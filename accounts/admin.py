"""Accounts admin."""
# Django
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):  # noqa: D101
    """User admin."""

    list_display = (
        'email',
        'username',
        'is_staff',
    )

    fieldsets = (
        ('Dane osobiste',
         {'fields': (
             'first_name',
             'last_name',
             'email',
             'username',
         )}),
        ('Ważne daty',
         {'fields': (
             'last_login',
             'date_joined',
         )}),
        ('Uprawnienia',
         {'fields': (
             'is_active',
             'is_staff',
             'is_superuser',
             'groups',
             'user_permissions',
         )}),
    )
