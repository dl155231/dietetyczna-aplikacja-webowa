"""Diet app views."""
# Standard Library
from datetime import date

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Project
from diet_app.forms import DietCreatorForm
from diet_app.models import Diet
from diet_app.models import DietDay


class MainView(LoginRequiredMixin, TemplateView):  # noqa: D101
    template_name = 'client_diet.html'

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super().get_context_data(**kwargs)
        if not self.request.user.nutritionist:
            try:
                diet = Diet.objects.get(user=self.request.user)
                context['diet_name'] = diet.name_diet
                if (date.today() - diet.day_zero).days == 0:
                    context['diet_day'] = 1
                else:
                    context['diet_day'] = (date.today() - diet.day_zero).days
                try:
                    context['meals'] = diet.dietday_set.get(day=date.today()).day_meals
                except DietDay.DoesNotExist:
                    context['meals'] = 'Brak'
            except Diet.DoesNotExist:
                return context
        return context


class NotificationListView(TemplateView):
    template_name = 'notification_list.html'

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super().get_context_data(**kwargs)

        return context


def main_page_redirect(request):
    """That view redirect to individual users's page."""
    if not request.user.is_anonymous and request.user.nutritionist != None:
        return  redirect('diet:diet_list', request.user.nutritionist.id)
    return redirect('diet:client_diet')


def diet_list(request, nut_id):
    try:
        diet_list = Diet.objects.filter(nutritionist_id=nut_id)
    except Diet.DoesNotExist:
        diet_list = None
    return render(request, 'diets_list.html', {'diet_list': diet_list})


def diet_creator(request, diet_id):
    diet = Diet.objects.get(id=diet_id)
    if request.method == 'GET':
        form_diet = DietCreatorForm(instance=diet)
    if request.method == 'POST':
        form_diet = DietCreatorForm(request.POST, instance=diet)
        if form_diet.is_valid():
            form_diet.save()

    return render(request, 'diet_creator.html', {'form_diet': form_diet})
