from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='home'),
    path('result', views.result_page, name='result'),
    path('result_stat_param2', views.result_stat_param2, name='result_stat_param2')
]