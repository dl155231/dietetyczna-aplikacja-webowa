"""Diet app urls."""
# Django
from django.urls import path

# Project
from diet_app.views import MainView, NotificationListView, diet_list, diet_creator, main_page_redirect, diet_days_list, \
    diet_creator_first, diet_day_creator, diet_day_creator_first, products_list

app_name = 'diet'
urlpatterns = [
    path('', main_page_redirect, name='main_page_redirect'),
    path('home/', MainView.as_view(), name='client_diet'),
    path('diet-list/<nut_id>/', diet_list, name='diet_list'),
    path('diet-creator-first/', diet_creator_first, name='diet_creator_first'),
    path('diet-creator/<diet_id>/', diet_creator, name='diet_creator'),
    path('diet-days-list/<diet_id>/', diet_days_list, name='diet_days'),
    path('diet-days-creator-first/<diet_id>/', diet_day_creator_first, name='diet_days_creator_first'),
    path('products-list/<diet_day_id>/', products_list, name='products_list'),
    path('diet-days-creator/<diet_id>/<diet_day_id>/', diet_day_creator, name='diet_days_creator'),
    path('notification-list/', NotificationListView.as_view(), name='notification_list'),
]
