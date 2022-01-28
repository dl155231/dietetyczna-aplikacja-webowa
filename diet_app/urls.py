"""Diet app urls."""
# Django
from django.urls import path

# 3rd-party
from diet_app.views import AcceptedConsultationsListView, SorryPageView
from diet_app.views import ConsultationsCreateView
from diet_app.views import ConsultationsListView
from diet_app.views import ConsultationsUpdateView
from diet_app.views import DietUserView
from diet_app.views import NotificationListView
from diet_app.views import ProductDetailView
from diet_app.views import diet_creator
from diet_app.views import diet_creator_first
from diet_app.views import diet_day_creator
from diet_app.views import diet_day_creator_first
from diet_app.views import diet_days_list
from diet_app.views import diet_list
from diet_app.views import main_page_redirect
from diet_app.views import nutrients_creator
from diet_app.views import product_creator
from diet_app.views import product_creator_first
from diet_app.views import products_list

app_name = 'diet'
urlpatterns = [
    path('', main_page_redirect, name='main_page_redirect'),  # noqa: E501
    path('home/', DietUserView.as_view(), name='client_diet'),  # noqa: E501
    path('sorry-page/', SorryPageView.as_view(), name='sorry_page'),  # noqa: E501
    path('notification-list/', NotificationListView.as_view(), name='notification_list'),  # noqa: E501
    path('diet-list/<nut_id>/', diet_list, name='diet_list'),  # noqa: E501
    path('diet-creator-first/', diet_creator_first, name='diet_creator_first'),  # noqa: E501
    path('product-detail/<product_id>/', ProductDetailView.as_view(), name='product_detail'),  # noqa: E501
    path('diet-creator/<diet_id>/', diet_creator, name='diet_creator'),  # noqa: E501
    path('diet-days-list/<diet_id>/', diet_days_list, name='diet_days'),  # noqa: E501
    path('diet-days-creator-first/<diet_id>/', diet_day_creator_first, name='diet_days_creator_first'),  # noqa: E501
    path('products-list/<diet_day_id>/<diet_id>/', products_list, name='products_list'),  # noqa: E501
    path('products-list-creator-first/<diet_day_id>/', product_creator_first, name='product_creator_first'),  # noqa: E501
    path('nutrients-creator/<product_id>/<diet_day_id>/', nutrients_creator, name='nutrients_creator'),  # noqa: E501
    path('products-list-creator/<diet_day_id>/<product_id>/', product_creator, name='products_creator'),  # noqa: E501
    path('diet-days-creator/<diet_id>/<diet_day_id>/', diet_day_creator, name='diet_days_creator'),  # noqa: E501
    path('notification-list/', NotificationListView.as_view(), name='notification_list'),  # noqa: E501
    path('consultations/create/', ConsultationsCreateView.as_view(), name='consultations_create'),  # noqa: E501
    path('consultations/list/', ConsultationsListView.as_view(), name='consultations_list'),  # noqa: E501
    path('consultations/edit/<pk>/', ConsultationsUpdateView.as_view(), name='consultations_edit'),  # noqa: E501
    path('consultations/accepted/list/', AcceptedConsultationsListView.as_view(), name='consultations_accepted_list'),  # noqa: E501
]
