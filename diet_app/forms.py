from django import forms

from diet_app.models import Diet, DietDay


class DietCreatorForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):  # noqa: D107
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_nutritionist(self):
        # nutritionist = self.cleaned_data.get('nutritionist')
        # print(nutritionist)
        # print(self.user.nutritionist)
        return self.user.nutritionist

    class Meta:  # noqa: D106
        model = Diet
        fields = '__all__'


class DayDietForm(forms.ModelForm):
    class Meta:  # noqa: D106
        model = DietDay
        fields = '__all__'
