def signs_criterum_res(count_pints, count):
    result1 = 'H1'
    result2 = 'H0'
    result3 = 'Слишком много данных!!! Полегче Амиго!!!'

    if count_pints >=8 and count_pints <=10:
        if count > 1:
            return result1
        else:
            return result2

    if count_pints >=11 and count_pints <=12:
        if count > 2:
            return result1
        else:
            return result2

    if count_pints >=13 and count_pints <=15:
        if count > 3:
            return result1
        else:
            return result2

    if count_pints >=16 and count_pints <=17:
        if count > 4:
            return result1
        else:
            return result2

    if count_pints >=18 and count_pints <=20:
        if count > 5:
            return result1
        else:
            return result2

    if count_pints >=21 and count_pints <=22:
        if count > 6:
            return result1
        else:
            return result2

    if count_pints >=23 and count_pints <=25:
        if count > 7:
            return result1
        else:
            return result2

    if count_pints >=26 and count_pints <=28:
        if count > 8:
            return result1
        else:
            return result2

    if count_pints == 29:
        if count > 9:
            return result1
        else:
            return result2

    if count_pints >=30 and count_pints <=32:
        if count > 10:
            return result1
        else:
            return result2

    if count_pints >=33 and count_pints <=34:
        if count > 11:
            return result1
        else:
            return result2


    if count_pints >=35:
        return result3