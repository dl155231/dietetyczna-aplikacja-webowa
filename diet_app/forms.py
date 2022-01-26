from django import forms

from diet_app.models import Diet, DietDay


class DietCreatorForm(forms.ModelForm):
    class Meta:  # noqa: D106
        model = Diet
        fields = '__all__'


class DayDietForm(forms.ModelForm):
    class Meta:  # noqa: D106
        model = DietDay
        fields = '__all__'
