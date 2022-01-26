"""Forms for the diet_app."""
# Django
from django import forms

# Project
from diet_app.models import Consultations
from diet_app.models import Diet
from diet_app.models import DietDay
from diet_app.models import Nutritionist


class DietCreatorForm(forms.ModelForm):  # noqa: D101

    def __init__(self, user, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.user = user

    nutritionist = forms.IntegerField(
        widget=forms.HiddenInput,
    )

    def clean_nutritionist(self):  # noqa: D102
        # nutritionist = self.cleaned_data.get('nutritionist')
        # print(nutritionist)
        # print(self.user.nutritionist)
        return self.user.nutritionist

    class Meta:  # noqa: D106
        model = Diet
        fields = '__all__'


class DayDietForm(forms.ModelForm):  # noqa: D101

    def __init__(self, diet, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.diet = diet

    diet = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput,
    )

    def clean_diet(self):  # noqa: D102
        return self.diet

    def clean_day(self):  # noqa: D102
        day = self.cleaned_data.get('day')
        if DietDay.objects.filter(day=day, diet_id=self.diet.id).exists():
            raise forms.ValidationError('Ta data jest już zajęta!')
        return day

    class Meta:  # noqa: D106
        model = DietDay
        fields = '__all__'


class ConsultationsForm(forms.ModelForm):  # noqa: D101
    def __init__(self, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.fields['nutritionist'].queryset = Nutritionist.objects.all()

    def form_valid(self, form):  # noqa: D102
        form.instance.client = self.request.user.client
        return super().form_valid(form)

    class Meta:  # noqa: D106
        model = Consultations
        fields = ['date', 'time', 'nutritionist']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'nutritionist': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
        }
