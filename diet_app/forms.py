"""Forms for the diet_app."""
# Django
from django import forms

# Project
from diet_app.models import Consultations, Nutrients
from diet_app.models import Diet
from diet_app.models import DietDay
from diet_app.models import Nutritionist
from diet_app.models import Diet, DietDay, Product


class DietCreatorForm(forms.ModelForm):  # noqa: D101

    def __init__(self, user, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.user = user

    nutritionist = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False,
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


class ProductForm(forms.ModelForm):

    def __init__(self, diet_day, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.diet_day = diet_day

    diet_day = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput,
    )

    def clean_diet_day(self):
        return self.diet_day

    class Meta:  # noqa: D106
        model = Product
        fields = '__all__'


class NutrientsForm(forms.ModelForm):

    def __init__(self, product, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.product = product

    product = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput,
    )

    def clean_product(self):
        return self.product

    class Meta:  # noqa: D106
        model = Nutrients
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
