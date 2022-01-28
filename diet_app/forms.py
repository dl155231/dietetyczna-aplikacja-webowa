"""Forms for the diet_app."""
# Django
from django import forms
from django.utils import timezone

# Project
from accounts.models import CustomUser
from diet_app.models import Consultations
from diet_app.models import Diet
from diet_app.models import DietDay
from diet_app.models import Nutrients
from diet_app.models import Nutritionist
from diet_app.models import Product
from diet_app.models import UserDetails


class DietCreatorForm(forms.ModelForm):  # noqa: D101
    nutritionist = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False,
    )

    def __init__(self, user, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['user'].queryset = CustomUser.objects.filter(
            nutritionist=None,
            client__consultations__is_accepted=True,
            client__consultations__nutritionist=self.user.nutritionist,
        ).distinct('pk')

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
        if day > self.diet.day_end or day < self.diet.day_end:
            raise forms.ValidationError('Ta data nie jest z zakresu dni diety!')
        return day

    class Meta:  # noqa: D106
        model = DietDay
        fields = '__all__'


class DayDietFormEdit(forms.ModelForm):  # noqa: D101

    def __init__(self, diet, diet_day, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.diet = diet
        self.diet_day = diet_day

    diet = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput,
    )

    day = forms.DateField(
        required=False,
        widget=forms.HiddenInput,
    )

    def clean_diet(self):  # noqa: D102
        return self.diet

    def clean_day(self):  # noqa: D102
        return self.diet_day.day

    class Meta:  # noqa: D106
        model = DietDay
        fields = '__all__'


class ProductForm(forms.ModelForm):  # noqa: D101

    def __init__(self, diet_day, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.diet_day = diet_day

    diet_day = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput,
    )

    def clean_diet_day(self):  # noqa: D102
        return self.diet_day

    class Meta:  # noqa: D106
        model = Product
        fields = '__all__'


class NutrientsForm(forms.ModelForm):  # noqa: D101

    def __init__(self, product, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.product = product

    product = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput,
    )

    def clean_product(self):  # noqa: D102
        return self.product

    class Meta:  # noqa: D106
        model = Nutrients
        fields = '__all__'


class ConsultationsForm(forms.ModelForm):  # noqa: D101
    def __init__(self, *args, **kwargs):  # noqa: D107
        client = kwargs.pop('client', None)
        super().__init__(*args, **kwargs)
        self.fields['nutritionist'].queryset = Nutritionist.objects.all()
        self.fields['date'].initial = timezone.localdate()
        self.fields['time'].initial = timezone.localtime().strftime('%H:%M')
        self.fields['client'].initial = client

    class Meta:  # noqa: D106
        model = Consultations
        fields = ['date', 'time', 'client', 'nutritionist']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'nutritionist': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
            'client': forms.HiddenInput(),
        }


class NutritionistConsultationsForm(forms.ModelForm):  # noqa: D101
    class Meta:
        model = Consultations
        fields = ['date', 'time', 'client', 'nutritionist', 'is_accepted']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'client': forms.Select(attrs={'class': 'form-control',
                                          'required': 'required',
                                          'disabled': 'disabled',
                                          }),
            'nutritionist': forms.Select(attrs={'class': 'form-control',
                                                'required': 'required',
                                                'disabled': 'disabled',
                                                }),
            'is_accepted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class UserDetailsForm(forms.ModelForm):  # noqa: D101

    # def __init__(self, *args, **kwargs):  # noqa: D107
    #     user = kwargs.pop('user', None)
    #
    #     super().__init__(*args, **kwargs)
    #     user_details = user.user_details
    #     print(user_details)
    #     for key, value in user_details.__dict__.items():
    #         if key != '_state' and key != 'id':
    #             self.fields[key].initial = value

    class Meta:
        model = UserDetails
        exclude = ['id']
