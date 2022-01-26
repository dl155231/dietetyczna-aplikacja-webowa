"""Diet app urls."""
# Django
from django.urls import path

# Project
from diet_app.views import MainView, NotificationListView, diet_list, diet_creator, main_page_redirect

app_name = 'diet'
urlpatterns = [
    path('', main_page_redirect, name='main_page_redirect'),
    path('home/', MainView.as_view(), name='client_diet'),
    path('diet-list/<nut_id>/', diet_list, name='diet_list'),
    path('diet-creator/<diet_id>/', diet_creator, name='diet_creator'),
    path('notification-list/', NotificationListView.as_view(), name='notification_list'),
]
