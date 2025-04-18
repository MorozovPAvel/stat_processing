from django.shortcuts import render, redirect
from . import result_signs_criterium as rsg
import pandas as pd


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



        if count_plus >= count_minus:
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

