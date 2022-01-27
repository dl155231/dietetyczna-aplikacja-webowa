"""Diet app views."""
# Standard Library
from datetime import date

# Django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

# Project
from diet_app.forms import ConsultationsForm
from diet_app.forms import DayDietForm
from diet_app.forms import DayDietFormEdit
from diet_app.forms import DietCreatorForm
from diet_app.forms import NutrientsForm
from diet_app.forms import ProductForm
from diet_app.models import Consultations
from diet_app.models import Diet
from diet_app.models import DietDay
from diet_app.models import Nutrients
from diet_app.models import Product


class DietUserView(LoginRequiredMixin, TemplateView):  # noqa: D101
    template_name = 'client_diet.html'

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super().get_context_data(**kwargs)
        if not self.request.user.nutritionist:
            try:
                diet = Diet.objects.get(user=self.request.user)
                context['diet_name'] = diet.name_diet
                if (date.today() - diet.day_zero).days == 0:
                    context['diet_day'] = 1
                elif (date.today() - diet.day_zero).days < 0:
                    context['diet_day'] = 0
                else:
                    context['diet_day'] = (date.today() - diet.day_zero).days
                try:
                    context['meals'] = diet.dietday_set.get(day=date.today()).day_meals
                except DietDay.DoesNotExist:
                    context['meals'] = 'Brak'
                try:
                    diet_day = DietDay.objects.get(day=date.today(), diet_id=diet.id)
                    product_list = Product.objects.filter(diet_day_id=diet_day.id)
                    context['products'] = product_list
                except:
                    context['products'] = None
            except Diet.DoesNotExist:
                return context
        return context


class NotificationListView(TemplateView):  # noqa: D101
    template_name = 'notification_list.html'

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super().get_context_data(**kwargs)

        return context


def main_page_redirect(request):
    """View redirect to individual users page."""
    # if not request.user.is_anonymous and request.user.nutritionist is not None:
    #     return redirect('diet:diet_list', request.user.nutritionist.id)
    # return redirect('diet:client_diet')
    return render(request, 'partials/opening_page.html', {})


def diet_list(request, nut_id):  # noqa: D103
    try:
        diet_list = Diet.objects.filter(nutritionist_id=nut_id)
    except Diet.DoesNotExist:
        diet_list = None
    return render(request, 'diets_list.html', {'diet_list': diet_list})


def diet_creator(request, diet_id):  # noqa: D103
    diet = Diet.objects.get(id=diet_id)
    try:
        user_nut_id = request.user.nutritionist.id
    except request.useruser.nutritionist.DoesNotExist:
        raise Http404

    if diet.nutritionist.id != user_nut_id:
        raise Http404
    if request.method == 'GET':
        form_diet = DietCreatorForm(instance=diet, user=request.user)
    if request.method == 'POST':
        form_diet = DietCreatorForm(data=request.POST, instance=diet, user=request.user)
        if form_diet.is_valid():
            form_diet.save()
            return redirect('diet:diet_list', request.user.nutritionist.id)

    return render(request, 'diet_creator.html', {'form_diet': form_diet, 'diet_id': diet_id, 'nut_id': user_nut_id})


def diet_creator_first(request):  # noqa: D103
    if request.method == 'GET':
        form_diet = DietCreatorForm(user=request.user)
    if request.method == 'POST':
        form_diet = DietCreatorForm(data=request.POST, user=request.user)
        if form_diet.is_valid():
            form_diet.save()
            return redirect('diet:diet_list', request.user.nutritionist.id)

    return render(request, 'diet_creator_first.html', {'form_diet': form_diet, 'nut_id': request.user.nutritionist.id})


def diet_days_list(request, diet_id):  # noqa: D103
    diet_days_list = DietDay.objects.filter(diet_id=diet_id)
    return render(request, 'diet_days_list.html',
                  {'diet_id': diet_id, 'diet_days_list': diet_days_list})


def diet_day_creator(request, diet_id, diet_day_id):  # noqa: D103
    diet_day = DietDay.objects.get(diet_id=diet_id, id=diet_day_id)
    diet = Diet.objects.get(id=diet_id)
    if request.method == 'GET':
        form_diet_day = DayDietFormEdit(instance=diet_day, diet=diet, diet_day=diet_day)
    if request.method == 'POST':
        form_diet_day = DayDietFormEdit(data=request.POST, instance=diet_day, diet=diet,
                                        diet_day=diet_day)
        if form_diet_day.is_valid():
            form_diet_day.save()
            return redirect('diet:diet_days', diet_id)

    return render(request,
                  'diet_day_creator.html', {
                      'form_diet_day': form_diet_day,
                      'diet_id': diet_id, 'diet_day_id': diet_day_id},
                  )


def diet_day_creator_first(request, diet_id):  # noqa: D103
    diet = Diet.objects.get(id=diet_id)
    if request.method == 'GET':
        form_diet_day = DayDietForm(diet=diet)
    if request.method == 'POST':
        form_diet_day = DayDietForm(data=request.POST, diet=diet)
        if form_diet_day.is_valid():
            form_diet_day.save()
            return redirect('diet:diet_days', diet_id)
    return render(request, 'diet_day_creator_first.html', {'form_diet_day': form_diet_day, 'diet_id': diet_id})


def products_list(request, diet_day_id, diet_id):  # noqa: D103
    products = Product.objects.filter(diet_day_id=diet_day_id)
    return render(request, 'products_list.html',
                  {'products': products, 'diet_day_id': diet_day_id, 'diet_id': diet_id})


class ConsultationsListView(LoginRequiredMixin, ListView):  # noqa: D101
    template_name = 'consultations_list.html'
    model = Consultations


class ConsultationsCreateView(LoginRequiredMixin, CreateView):  # noqa: D101
    template_name = 'consultations_create.html'
    model = Consultations
    form_class = ConsultationsForm

    def get_success_url(self):  # noqa: D102
        messages.success(self.request, 'Wysłano zgłoszenie')
        return reverse_lazy('diet:client_diet')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['client'] = self.request.user.client
        return kwargs

    def form_valid(self, form):  # noqa: D102
        print(form.cleaned_data['client'])
        form.instance.client = form.cleaned_data['client']
        return super().form_valid(form)


class ConsultationsUpdateView(LoginRequiredMixin, UpdateView):  # noqa: D101
    template_name = 'consultations_edit.html'
    model = Consultations
    form_class = ConsultationsForm

    def get_success_url(self):  # noqa: D102
        messages.success(self.request, 'Zmiany zapisane')
        return reverse_lazy('diet:client_diet')


class AcceptedConsultationsListView(LoginRequiredMixin, ListView):
    model = Consultations
    template_name = 'accepted_consultations_list.html'

    def get_queryset(self):  # noqa: D102
        return Consultations.objects.filter(
            nutritionist=self.request.user.nutritionist,
            is_accepted=True,
            client__isnull=False,
        )


def product_creator(request, diet_day_id, product_id):
    product = Product.objects.get(id=product_id)
    diet_day = DietDay.objects.get(id=diet_day_id)
    if request.method == 'GET':
        form_product = ProductForm(instance=product, diet_day=diet_day)
    if request.method == 'POST':
        form_product = ProductForm(data=request.POST, instance=product, diet_day=diet_day)
        if form_product.is_valid():
            form_product.save()
            return redirect('diet:products_list', diet_day_id, diet_day.diet.id)
    return render(request, 'product_creator.html',
                  {'form_product': form_product, 'product_id': product_id,
                   'diet_day_id': diet_day_id, 'diet_id': diet_day.diet.id},
                  )


def product_creator_first(request, diet_day_id):
    diet_day = DietDay.objects.get(id=diet_day_id)
    if request.method == 'GET':
        form_product = ProductForm(diet_day=diet_day)
    if request.method == 'POST':
        form_product = ProductForm(data=request.POST, diet_day=diet_day)
        if form_product.is_valid():
            form_product.save()
            return redirect('diet:products_list', diet_day_id, diet_day.diet.id)
    return render(request, 'product_creator_first.html', {'form_product': form_product, 'diet_day_id': diet_day_id, 'diet_id': diet_day.diet.id})


def nutrients_creator(request, product_id, diet_day_id):
    product = Product.objects.get(id=product_id)
    if Nutrients.objects.filter(product_id=product_id).exists():
        nutrients = Nutrients.objects.get(product_id=product_id)
        if request.method == 'GET':
            form_nutrients = NutrientsForm(instance=nutrients, product=product)
        if request.method == 'POST':
            form_nutrients = NutrientsForm(data=request.POST, instance=nutrients, product=product)
            if form_nutrients.is_valid():
                form_nutrients.save()
                return redirect('diet:products_list', diet_day_id, product.diet_day.diet.id)
    else:
        if request.method == 'GET':
            form_nutrients = NutrientsForm(product=product)
        if request.method == 'POST':
            form_nutrients = NutrientsForm(data=request.POST, product=product)
            if form_nutrients.is_valid():
                form_nutrients.save()
                return redirect('diet:products_list', diet_day_id, product.diet_day.diet.id)
    return render(request, 'nutrients_creator.html', {'form_nutrients': form_nutrients, 'diet_day_id': diet_day_id, 'diet_id': product.diet_day.diet.id})


class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['product_id']
        try:
            nutrients = Nutrients.objects.get(product_id=int(product_id))
        except Nutrients.DoesNotExist:
            nutrients = None
        context['nutrients'] = nutrients
        return context
