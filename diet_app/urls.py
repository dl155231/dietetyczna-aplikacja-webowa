"""Diet app urls."""
# Django
from django.urls import path

# Project
from diet_app.views import ConsultationsCreateView, ConsultationsUpdateView
from diet_app.views import ConsultationsListView
from diet_app.views import MainView
from diet_app.views import NotificationListView
from diet_app.views import diet_creator
from diet_app.views import diet_creator_first
from diet_app.views import diet_day_creator
from diet_app.views import diet_day_creator_first
from diet_app.views import diet_days_list
from diet_app.views import diet_list
from diet_app.views import main_page_redirect
from diet_app.views import products_list

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
    path('consultations/list/', ConsultationsListView.as_view(), name='consultations_list'),
    path('consultations/create/', ConsultationsCreateView.as_view(), name='consultations_create'),
    path('consulations/edit/<pk>/', ConsultationsUpdateView.as_view(), name='consultations_edit'),
]
