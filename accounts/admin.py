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
             'password',
         )}),
        ('Ważne daty',
         {'fields': (
             'last_login',
             'date_joined',
         )}),
        ('Uprawnienia',
         {'fields': (
             'is_superuser',
             'is_staff',
             'is_active',
             'is_nutritionist',
             'groups',
             'user_permissions',
             'nutritionist',
         )}),
    )
