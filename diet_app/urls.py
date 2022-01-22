from django.urls import path

from diet_app.views import ClientDietView

urlpatterns = [
    path('diet/', ClientDietView.as_view(), name='client_diet'),
]