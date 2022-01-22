"""Diet app admin."""
# Django
from django.contrib import admin

# Project
from diet_app.models import Client
from diet_app.models import Diet
from diet_app.models import Nutrients
from diet_app.models import Nutritionist
from diet_app.models import Product
from diet_app.models import UserDetails
from diet_app.models import Vitamin
from diet_app.models import WaterConsumption


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(Vitamin)
class VitaminAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(Nutrients)
class NutrientsAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(Nutritionist)
class NutritionistAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):  # noqa: D101
    pass


@admin.register(WaterConsumption)
class WaterConsumptionAdmin(admin.ModelAdmin):  # noqa: D101
    pass
