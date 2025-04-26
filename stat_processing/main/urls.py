from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='home'),
    path('parametric_criterium', views.parametric_criterium, name='parametric_criterium'),
    path('no_parametric_criterium', views.no_parametric_criterium, name='no_parametric_criterium'),
    path('descriptive_statistics', views.descriptive_statistics, name='descriptive_statistics'),
    path('normal_distribution', views.normal_distribution, name='normal_distribution'),
    path('result', views.result_sings_criterium, name='result'),
    path('result_stat_param2', views.result_stydent_criterium, name='result_stat_param2'),
    path('result_stat_param3', views.result_stat_param3, name='result_stat_param3')
]