from django.urls import path

from diet_app.views import ClientDietView

app_name = 'diet'
urlpatterns = [
    path('diet/', ClientDietView.as_view(), name='client_diet'),
]