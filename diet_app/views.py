"""Diet app views."""
# Standard Library
from datetime import date

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Project
from diet_app.forms import DietCreatorForm, DayDietForm
from diet_app.models import Diet, Product
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
        form_diet = DietCreatorForm(instance=diet, user=request.user)
    if request.method == 'POST':
        form_diet = DietCreatorForm(data=request.POST, instance=diet, user=request.user)
        if form_diet.is_valid():
            form_diet.save()

    return render(request, 'diet_creator.html', {'form_diet': form_diet, 'diet_id': diet_id})


def diet_creator_first(request):
    if request.method == 'GET':
        form_diet = DietCreatorForm(user=request.user)
    if request.method == 'POST':
        form_diet = DietCreatorForm(data=request.POST, user=request.user)
        if form_diet.is_valid():
            form_diet.save()
            return redirect('diet:diet_list', request.user.nutritionist.id )

    return render(request, 'diet_creator_first.html', {'form_diet': form_diet})


def diet_days_list(request, diet_id):
    diet_days_list = DietDay.objects.filter(diet_id=diet_id)
    return render(request, 'diet_days_list.html', {'diet_id': diet_id, 'diet_days_list': diet_days_list})


def diet_day_creator(request, diet_id, diet_day_id):
    diet_day = DietDay.objects.get(diet_id=diet_id, id=diet_day_id)
    diet = Diet.objects.get(id=diet_id)
    if request.method == 'GET':
        form_diet_day = DayDietForm(instance=diet_day, diet=diet)
    if request.method == 'POST':
        form_diet_day = DayDietForm(data=request.POST, instance=diet_day, diet=diet)
        if form_diet_day.is_valid():
            form_diet_day.save()
            return redirect('diet:diet_days', diet_id)

    return render(request, 'diet_day_creator.html', {'form_diet_day': form_diet_day, 'diet_id': diet_id, 'diet_day_id': diet_day_id})


def diet_day_creator_first(request, diet_id):
    diet = Diet.objects.get(id=diet_id)
    if request.method == 'GET':
        form_diet_day = DayDietForm(diet=diet)
    if request.method == 'POST':
        form_diet_day = DayDietForm(data=request.POST, diet=diet)
        if form_diet_day.is_valid():
            form_diet_day.save()
            return redirect('diet:diet_days', diet_id)
    return render(request, 'diet_day_creator_first.html', {'form_diet_day': form_diet_day})


def products_list(request, diet_day_id):
    products = Product.objects.filter(diet_day_id=diet_day_id)
    return render(request, 'products_list.html', {'products': products, 'diet_day_id': diet_day_id})
