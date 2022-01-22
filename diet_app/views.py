from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from diet_app.models import Diet


class ClientDietView(TemplateView):
    template_name = 'client_diet.html'

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            diet = Diet.objects.get(user=self.request.user)
            context['diet_name'] = diet.name_diet
        return context

