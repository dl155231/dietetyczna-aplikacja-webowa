"""Diet app urls."""
# Django
from django.urls import path

# Project
from diet_app.views import MainView, NotificationListView

app_name = 'diet'
urlpatterns = [
    path('home/', MainView.as_view(), name='client_diet'),
    path('notification-list/', NotificationListView.as_view(), name='notification_list'),
]
