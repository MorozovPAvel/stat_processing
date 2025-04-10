from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='home'),
    path('result', views.result_page, name='result')
]