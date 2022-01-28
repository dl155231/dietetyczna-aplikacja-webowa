"""Diet utils."""
# Standard Library
import datetime

# Django
from django.core.exceptions import ValidationError


def present_or_future_date(value):  # noqa: 103
    if value < datetime.date.today():
        raise ValidationError('Data nie może być w przeszłości!')
    return value
