def get_result_coef_e_a(len_list, assimetric, ekscess):
    result = 'Выборка не подчиняется закону нормального распределения'

    result2 = 'Выборка подчиняется закону нормального распределения'

    assimetric_r = 0

    ekscess_r = 0

    if len_list <= 13:
        assimetric_r = 0.71
        ekscess_r = 0.9
        if assimetric < 0.71 and ekscess < 0.9:
            result = result2


    if 13 < len_list <= 18:
        assimetric_r = 0.71
        ekscess_r = 0.88
        if assimetric < 0.71 and ekscess < 0.88:
            result = result2

    if 18 < len_list <= 23:
        assimetric_r = 0.71
        ekscess_r = 0.87
        if assimetric < 0.71 and ekscess < 0.87:
            result = result2

    if 23 < len_list <= 28:
        assimetric_r = 0.71
        ekscess_r = 0.86
        if assimetric < 0.71 and ekscess < 0.86:
            result = result2

    if 28 < len_list <= 32:
        assimetric_r = 0.61
        ekscess_r = 0.86
        if assimetric < 0.61 and ekscess < 0.86:
            result = result2

    if 32 < len_list <= 38:
        assimetric_r = 0.62
        ekscess_r = 0.85
        if assimetric < 0.62 and ekscess < 0.85:
            result = result2

    if 38 < len_list <= 43:
        assimetric_r = 0.58
        ekscess_r = 0.85
        if assimetric < 0.58 and ekscess < 0.85:
            result = result2

    if 43 < len_list <= 48:
        assimetric_r = 0.55
        ekscess_r = 0.85
        if assimetric < 0.55 and ekscess < 0.85:
            result = result2

    if 48 < len_list <= 55:
        assimetric_r = 0.53
        ekscess_r = 0.84
        if assimetric < 0.53 and ekscess < 0.84:
            result = result2

    if 55 < len_list <= 65:
        assimetric_r = 0.49
        ekscess_r = 0.84
        if assimetric < 0.49 and ekscess < 0.84:
            result = result2

    if 65 < len_list <= 75:
        assimetric_r = 0.45
        ekscess_r = 0.84
        if assimetric < 0.45 and ekscess < 0.84:
            result = result2

    if 75 < len_list <= 85:
        assimetric_r = 0.43
        ekscess_r = 0.84
        if assimetric < 0.43 and ekscess < 0.84:
            result = result2

    if 85 < len_list <= 95:
        assimetric_r = 0.40
        ekscess_r = 0.83
        if assimetric < 0.40 and ekscess < 0.83:
            result = result2

    if 95 < len_list <= 125:
        assimetric_r = 0.35
        ekscess_r = 0.83
        if assimetric < 0.35 and ekscess < 0.83:
            result = result2

    return result, assimetric_r, ekscess_r