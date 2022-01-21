"""Admin file."""
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