from django import forms

from diet_app.models import Diet, DietDay


class DietCreatorForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.user = user

    nutritionist = forms.IntegerField(
        widget=forms.HiddenInput,
    )

    def clean_nutritionist(self):
        # nutritionist = self.cleaned_data.get('nutritionist')
        # print(nutritionist)
        # print(self.user.nutritionist)
        return self.user.nutritionist

    class Meta:  # noqa: D106
        model = Diet
        fields = '__all__'


class DayDietForm(forms.ModelForm):

    def __init__(self, diet, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.diet = diet

    diet = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput,
    )

    def clean_diet(self):
        return self.diet

    def clean_day(self):
        day = self.cleaned_data.get('day')
        if DietDay.objects.filter(day=day, diet_id=self.diet.id).exists():
            raise forms.ValidationError('Ta data jest już zajęta!')
        return day

    class Meta:  # noqa: D106
        model = DietDay
        fields = '__all__'
