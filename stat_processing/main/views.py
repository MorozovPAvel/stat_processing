from django.shortcuts import render, redirect
from statistics import mode, median, stdev, variance
import scipy
from scipy.stats import skew
from scipy.stats import kurtosis
from . import result_signs_criterium as rsg
from . import result_student_criterium as rsc
from . import get_standart_error as gse
import pandas as pd
import math


def index(request):
    return render(request, 'main/index.html', {'title': 'МедМатСтат (Стартоваая страница)',
                                               'task_group': 'Выбери раздел',
                                               'name_page': 'Медицинская статистика',
                                               'tasks': 'Выбери метод из представленных ниже'})

def parametric_criterium(request):
    return render(request, 'main/parametric_criterium.html', {'title': 'МедМатСтат (Параметрические критерии)',
                                               'task_group':'Выбери раздел',
                                               'name_page': 'Параметрические критерии',
                                               'tasks': 'Выбери метод из представленных ниже'})

def no_parametric_criterium(request):
    return render(request, 'main/no_parametric_criterium.html', {'title': 'МедМатСтат (Непраметрические критерии)',
                                               'task_group':'Выбери раздел',
                                               'name_page': 'Непараместрические критерии',
                                               'tasks': 'Выбери метод из представленных ниже'})
def normal_distribution(request):
    return render(request, 'main/normal_distribution.html', {'title': 'МедМатСтат (Нормальное распределение)',
                                               'task_group':'Выбери раздел',
                                               'name_page': 'Нормальное распределение',
                                               'tasks': 'Выбери метод из представленных ниже'})

def descriptive_statistics(request):
    return render(request, 'main/descriptive_statistics.html', {'title': 'МедМатСтат (Описательная статистика)',
                                               'task_group':'Выбери раздел',
                                               'name_page': 'Описательная статистика',
                                               'tasks': 'Выбери метод из представленных ниже'})

def result_sings_criterium(request):
    result = ''
    try:
        param1 = request.POST['first_param']
        param2 = request.POST['second_param']

        stroke = []
        stroke_param1 = param1.split()
        stroke_param2 = param2.split()

        count_points = 0
        count_plus = 0
        count_minus = 0

        for i1, i2 in zip(stroke_param1, stroke_param2):
            s = ''
            if float(i1) < float(i2):
                s = '+'
                count_plus = count_plus + 1
            if float(i1) > float(i2):
                s = '-'
                count_minus = count_minus + 1
            if float(i1) == float(i2):
                s = '='

            count_points = count_points + 1
            stroke.append({'par1': i1, 'par2': i2, 'par3': s})



        if count_plus <= count_minus:
            result = rsg.signs_criterum_res(count_points, count_plus)
        else:
            result = rsg.signs_criterum_res(count_points, count_minus)

        if count_points < 8:
            result = 'Недостаточно данных, введите больше значений'

    except:
        result = 'Что-то пошло не так, проверьте введенные данные'
        stroke = []
    return render(request, 'main/result_sings_ctiterium.html', {'result': result,
                                                'title': 'МедМатСтат',
                                                'table': stroke,
                                                'count_plus': count_plus,
                                                'count_minus': count_minus})

def result_stydent_criterium(request):
    #result = 'В этом расчете пока ничего нет! Ведутся работы!!!!'

    try:
        param1 = request.POST['first_param']
        param2 = request.POST['second_param']

        stroke = []
        stroke_param1 = list(map(int, param1.split()))
        stroke_param2 = list(map(int, param2.split()))

        if len(stroke_param1) == len(stroke_param2) or len(stroke) >= 9 or len(stroke) <= 30:
            #находим среднее значение для введенных массивов
            average1 = round(sum(stroke_param1) / len(stroke_param1), 2)
            average2 = round(sum(stroke_param2) / len(stroke_param2), 2)

            #вычисляем стандартную ошибку
            standart_error_num1 = round(gse.resurn_se(stroke_param1, average1), 2)
            standart_error_num2 = round(gse.resurn_se(stroke_param2, average2), 2)

            t_crtterium = round(abs(average1 - average2) / math.sqrt((standart_error_num1 ** 2) + (standart_error_num2 ** 2)), 2)

            result, t_crit = rsc.get_result(len(stroke_param1), t_crtterium)

            result1 = f"avg {average1}, {average2}, se {standart_error_num1} {standart_error_num2}, f {t_crtterium}"

            for i1, i2 in zip(stroke_param1, stroke_param2):
                stroke.append({'par1': i1, 'par2': i2})


        else:
            result = 'Количество данных должно совпадать в обоих слобцах! Либо слишком мало/много данных'

    except:
        print('ОШИБКА')
        result = 'Что-то пошло не так, проверьте введенные данные'
        t_crit = ''
        result1 = ''
        stroke = []
        t_crtterium = ''

    return render(request, 'main/result_stydent_ctiterium.html', {'result': result,
                                                                        't_crit': t_crit,
                                                                        'title': 'МедМатСтат',
                                                                        'risevalue': result1,
                                                                        'table': stroke,
                                                                        't_crtterium': t_crtterium})


def result_descriptive_statistics(request):
    result = 'Что-то пошло не так, проверьте введенные данные!!!'
    average = 0
    stroke = []
    standart_error = 0
    moda = 0
    mediana = 0
    standart_dev = 0
    dispersia = 0
    assimetric = 0
    ekscess = 0
    interval = 0
    min_val = 0
    max_val = 0
    summ_val = 0
    count_val = 0

    try:
        result = ''
        param = request.POST['first_param']


        stroke_param = list(map(int, param.split()))
        for i1 in stroke_param:
            stroke.append({'par1': i1})

        average = round(sum(stroke_param) / len(stroke_param), 2)

        standart_error = round(gse.resurn_se(stroke_param, average), 2)

        moda = mode(stroke_param)

        mediana = median(stroke_param)

        standart_dev = round(stdev(stroke_param), 2)

        dispersia = round(variance(stroke_param), 2)

        assimetric = round(skew(stroke_param, axis=0, bias=True), 2)

        ekscess = round(kurtosis(stroke_param, axis=0, bias=True), 2)

        interval = max(stroke_param) - min(stroke_param)

        min_val = min(stroke_param)

        max_val = max(stroke_param)

        summ_val = sum(stroke_param)

        count_val = len(stroke_param)

    except:
        print('ERROR in result_descriptive_statistics')
        result = 'Что-то пошло не так, проверьте введенные данные!!!'


    return render(request, 'main/result_descriptive_statistics.html', {'result': result,
                                                                       'title': 'МедМатСтат',
                                                                       'table': stroke,
                                                                       'mediana': mediana,
                                                                       'standart_error': standart_error,
                                                                       'moda': moda,
                                                                       'interval': interval,
                                                                       'min_val': min_val,
                                                                       'max_val': max_val,
                                                                       'dispersia': dispersia,
                                                                       'standart_dev': standart_dev,
                                                                       'assimetric': assimetric,
                                                                       'ekscess': ekscess,
                                                                       'summ_val': summ_val,
                                                                       'count_val': count_val,
                                                                       'avg': average})
