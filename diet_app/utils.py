from diet_app.models import Nutritionist


def check_user(user):
    is_client = True
    if user.is_authenticated:
        try:
            if Nutritionist.objects.get(user=user):
                is_client = False
        except Nutritionist.DoesNotExist:
            is_client = True
    return is_client
