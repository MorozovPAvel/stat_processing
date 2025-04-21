from django.shortcuts import render, redirect
from . import result_signs_criterium as rsg
from . import result_student_criterium as rsc
from . import get_standart_error as gse
import pandas as pd
import math


#py manage.py runserver

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'title': 'Стат обработка',
                                               'tasks': 'Выбери метод из представленных ниже'})


def result_page(request):
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
    return render(request, 'main/result.html', {'result': result,
                                                'table': stroke,
                                                'count_plus': count_plus,
                                                'count_minus': count_minus})

def result_stat_param2(request):
    result = 'В этом расчете пока ничего нет! Ведутся работы!!!!'

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

    return render(request, 'main/result2.html', {'result': result,
                                                                        't_crit': t_crit,
                                                                        'risevalue': result1,
                                                                        'table': stroke,
                                                                        't_crtterium': t_crtterium})