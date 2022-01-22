"""Diet app views."""
# Standard Library
from datetime import date

# Django
from django.views.generic import TemplateView

# Project
from diet_app.models import Diet
from diet_app.models import DietDay
from diet_app.utils import check_user


class MainView(TemplateView):  # noqa: D101
    template_name = 'client_diet.html'

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            if check_user(self.request.user):
                try:
                    diet = Diet.objects.get(user=self.request.user)
                    context['diet_name'] = diet.name_diet
                    context['diet_day'] = (date.today()-diet.day_zero).days
                    try:
                        context['meals'] = diet.dietday_set.get(day=date.today()).day_meals
                    except DietDay.DoesNotExist:
                        context['meals'] = 'Brak'
                except Diet.DoesNotExist:
                    return context
            else:
                return context
        return context


class NotificationListView(TemplateView):
    template_name = 'notification_list.html'

    # def get_context_data(self, **kwargs):  # noqa: D102
    #     context = super().get_context_data(**kwargs)
    #     if not self.request.user.is_anonymous:
    #         if not check_user(self.request.user):
    #             # context['notifications'] =  tu bedzie lista zgloszen!
    #             return context
    #     return context
