from accounts.models import CustomUser


def extra_content(request):
    is_client = True
    if not request.user.is_anonymous and  request.user.nutritionist:
        is_client = False
    return {
        'is_client': is_client,
    }
