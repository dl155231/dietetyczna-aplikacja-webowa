"""API models."""

# Standard Library
from datetime import date

# Django
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

# Project
from diet_app.utils import present_or_future_date


class Nutritionist(models.Model):  # noqa: D101
    bank_account = models.CharField(
        verbose_name=_('Konto bankowe'),
        max_length=255,
    )

    competence_proof = models.FileField(
        upload_to='competence/',
        verbose_name=_('Potwierdzenie kompetencji'),
        null=True,  # tylko na potrzeby prezentacji projektu
        blank=True,  # tylko na potrzeby prezentacji projektu
    )

    class Meta:  # noqa: D106
        verbose_name = _('Dietetyk')
        verbose_name_plural = _('Dietetycy')

    def __str__(self):  # noqa: D105
        try:
            name = self.customuser.get_full_name()
        except:  # noqa: E722
            name = self.id
        return str(name)


class Diet(models.Model):  # noqa: D101

    meal_count = models.IntegerField(
        verbose_name=_('Ilość posiłków'),
    )

    calories = models.CharField(
        max_length=45,
        verbose_name=_('Kalorie'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Użytkownik'),
    )

    day_zero = models.DateField(
        verbose_name=_('Początek diety'),
        default=date.today,
    )
    day_end = models.DateField(
        verbose_name=_('Koniec diety'),
        default=date.today,
    )

    name_diet = models.CharField(
        max_length=255,
        verbose_name=_('Nazwa diety'),
        null=True,
    )

    nutritionist = models.ForeignKey(
        Nutritionist,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Dietetyk'),
    )

    class Meta:  # noqa: D106
        verbose_name = _('Dieta')
        verbose_name_plural = _('Diety')

    def __str__(self):  # noqa: D105
        return str(self.meal_count)


class DietDay(models.Model):  # noqa: D101
    day_meals = models.TextField(
        verbose_name=_('Dzienne posiłki'),
    )
    day = models.DateField(
        default=date.today,
        verbose_name=_('Dzień diety'),
    )
    diet = models.ForeignKey(
        Diet,
        null=True,
        blank=True,
        verbose_name=_('Dieta'),
        on_delete=models.SET_NULL,
    )

    class Meta:  # noqa: D106
        verbose_name = _('Dzień diety')
        verbose_name_plural = _('Dni diety')

    def __str__(self):  # noqa: D105
        return str(self.day)


class Product(models.Model):  # noqa: D101
    calories = models.IntegerField(
        verbose_name=_('Kalorie'),
    )

    product_name = models.CharField(
        max_length=255,
        verbose_name=_('Nazwa produktu'),
    )

    diet_day = models.ForeignKey(
        DietDay,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Dzień diety'),
    )

    class Meta:  # noqa: D106
        verbose_name = _('Produkt')
        verbose_name_plural = _('Produkty')

    def __str__(self):  # noqa: D105
        return str(self.product_name) + '|' + str(self.diet_day)


class Nutrients(models.Model):  # noqa: D101
    carbohydrate = models.IntegerField(
        verbose_name=_('Węglowodany'),
    )

    proteins = models.IntegerField(
        verbose_name=_('Białko'),
    )

    total_fat = models.IntegerField(
        verbose_name=_('Tłuszcze'),
    )

    saturated_fat = models.IntegerField(
        verbose_name=_('Tłuszcze nasycone'),
    )

    sugars = models.IntegerField(
        verbose_name=_('Cukry'),
    )

    vitamins = models.TextField(
        verbose_name=_('Witaminy'),
        null=True,
        blank=True,
    )

    fibers = models.IntegerField(
        verbose_name=_('Błonnik'),
    )

    product = models.OneToOneField(
        Product,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Produkt'),
    )

    class Meta:  # noqa: D106
        verbose_name = _('Wartości odżywcze')
        verbose_name_plural = _('Wartości odżywcze')

    def __str__(self):  # noqa: D105
        return str(self.product)


class Client(models.Model):  # noqa: D101
    user = models.OneToOneField(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        default=None,
    )
    phone_number = models.CharField(max_length=20)

    class Meta:  # noqa: D106
        verbose_name = _('Klient')
        verbose_name_plural = _('Klienci')

    def __str__(self):  # noqa: D105
        return f'{self.user.get_full_name()}'


class UserDetails(models.Model):  # noqa: D101
    CHOICES = (
        ('male', _('Mężczyzna')),
        ('female', _('Kobieta')),
        ('other', _('Inna')),
    )

    weight_current = models.IntegerField(
        verbose_name=_('Aktualna waga'),
    )

    height = models.IntegerField(
        verbose_name=_('Wzrost'),
    )

    age = models.IntegerField(
        verbose_name=_('Wiek'),
    )

    sex = models.TextField(
        verbose_name=_('Płeć'),
        max_length=9,
        choices=CHOICES,
        default='other',
    )

    weight_target = models.IntegerField(
        verbose_name=_('Waga docelowa'),
    )

    physical_activity = models.CharField(
        max_length=1000,
        verbose_name=_('Aktywność fizyczna'),
    )

    weight_week_loss = models.IntegerField(
        verbose_name=_('Tygodniowa strata wagi'),
    )

    allergies = models.CharField(
        max_length=1000,
        verbose_name=_('Alergie'),
    )

    illnesses = models.CharField(
        max_length=1000,
        verbose_name=_('Choroby'),
    )

    class Meta:  # noqa: D106
        verbose_name = _('Szczegóły użytkownika')
        verbose_name_plural = _('Szczegóły użytkownika')

    def __str__(self):  # noqa: D105
        return str(self.weight_current)


class WaterConsumption(models.Model):  # noqa: D101

    value = models.FloatField(
        verbose_name=_('Ilość'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Użytkownik'),
    )

    class Meta:  # noqa: D106
        verbose_name = _('Zużycie wody')
        verbose_name_plural = _('Zużycia wody')

    def __str__(self):  # noqa: D105
        return self.user


class Consultations(models.Model):  # noqa: D101

    date = models.DateField(
        verbose_name=_('Data'),
        validators=[present_or_future_date],
    )

    time = models.TimeField(
        verbose_name=_('Godzina'),
    )

    client = models.ForeignKey(
        Client,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Klient'),
    )

    nutritionist = models.ForeignKey(
        Nutritionist,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Dietetyk'),
    )

    is_accepted = models.BooleanField(
        _('Zaakceptowane'),
        default=False,
    )

    class Meta:  # noqa: D106
        verbose_name = _('Konsultacja')
        verbose_name_plural = _('Konsultacje')
        ordering = ['-date']

    def __str__(self):  # noqa: D105
        return f'Zgłoszenie konsultacji nr {self.id}'
