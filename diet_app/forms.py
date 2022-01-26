from django import forms

from diet_app.models import Diet


class DietCreatorForm(forms.ModelForm):
    class Meta:  # noqa: D106
        model = Diet
        fields = '__all__';
