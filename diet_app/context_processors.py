"""Context processors for the Diet App."""


def extra_content(request):  # noqa: D103
    is_client = True
    if not request.user.is_anonymous and request.user.nutritionist:
        is_client = False
    return {
        'is_client': is_client,
    }
