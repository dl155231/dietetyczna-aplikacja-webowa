"""Diet app urls."""
# Django
from django.urls import path

# Project
from diet_app.views import MainView, NotificationListView, diet_list, diet_creator, main_page_redirect, diet_days_list, \
    diet_creator_first

app_name = 'diet'
urlpatterns = [
    path('', main_page_redirect, name='main_page_redirect'),
    path('home/', MainView.as_view(), name='client_diet'),
    path('diet-list/<nut_id>/', diet_list, name='diet_list'),
    path('diet-creator-first/', diet_creator_first, name='diet_creator_first'),
    path('diet-creator/<diet_id>/', diet_creator, name='diet_creator'),
    path('diet-days-list/<diet_id>/', diet_days_list, name='diet_days'),
    path('notification-list/', NotificationListView.as_view(), name='notification_list'),
]
