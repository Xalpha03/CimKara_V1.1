from django.urls import path
from .views import *
from django.http import HttpResponse
from django.contrib.auth.models import User



# app_name = 'data'
urlpatterns = [
    path('', list_View.as_view(), name='list'),
    path('details/<str:user>', detail_View.as_view(), name='details'),
    path('update/<int:pk>/', update_View.as_view(), name='update'),
    path('delete/<int:pk>/', delete_View.as_view(), name='delete'),
    path('create/', create_View.as_view(), name='create'),
    path('filter/<str:user>/', filter_year_View.as_view(), name='filter'),
    path('weeks/', week_View.as_view(), name='weeks'),
    path('yesterday/', yesterday_View.as_view(), name='yesterday'),
    path('month/', month_View.as_view(), name='month'),
    path('year/', year_View.as_view(), name='year'),
    path('admin_view/', admin_View.as_view(), name='admin_view'),
    path('admin_update/<int:pk>/', admin_update_View.as_view(), name='admin_update'),
    path('admin_delete/<int:pk>/', admin_delete_View.as_view(), name='admin_delete'),
    
    
]