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
    path('result_stydent_criterium', views.result_stydent_criterium, name='result_stydent_criterium'),
    path('result_spearmanr_criterium', views.result_spearmanr_criterium, name='result_spearmanr_criterium'),
    path('result_coef_ekscess_assimmetric', views.result_coef_ekscess_assimmetric, name='result_coef_ekscess_assimmetric'),
    path('result_descriptive_statistics', views.result_descriptive_statistics, name='result_descriptive_statistics')
]