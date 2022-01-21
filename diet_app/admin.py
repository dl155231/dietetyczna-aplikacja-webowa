from django.contrib import admin

from diet_app.models import Diet, Product, Vitamin, Nutrients, Client, Nutritionist, UserDetails, WaterConsumption


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
