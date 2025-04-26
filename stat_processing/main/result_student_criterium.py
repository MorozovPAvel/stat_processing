

def get_result(len_s, t_criterium):
    result0 = 'H1 (t-эмперическое > t-критическое)'
    result1 = 'H0 (t-эмперическое < t-критическое)'
    if len_s == 9:
        if t_criterium > 2.30:
            return result0, 2.30
        else:
            return result1, 2.30
    if len_s == 10:
        if t_criterium > 2.26:
            return result0, 2.26
        else:
            return result1, 2.26
    if len_s == 11:
        if t_criterium > 2.22:
            return result0, 2.22
        else:
            return result1, 2.22
    if len_s == 12:
        if t_criterium > 2.20:
            return result0, 2.20
        else:
            return result1, 2.20
    if len_s == 13:
        if t_criterium > 2.17:
            return result0, 2.17
        else:
            return result1, 2.17
    if len_s == 14:
        if t_criterium > 2.16:
            return result0, 2.16
        else:
            return result1, 2.16
    if len_s == 15:
        if t_criterium > 2.14:
            return result0, 2.14
        else:
            return result1, 2.14
    if len_s == 16:
        if t_criterium > 2.13:
            return result0, 2.13
        else:
            return result1, 2.13
    if len_s == 17:
        if t_criterium > 2.11:
            return result0, 2.11
        else:
            return result1, 2.11
    if len_s == 18:
        if t_criterium > 2.10:
            return result0, 2.10
        else:
            return result1, 2.10
    if len_s == 19:
        if t_criterium > 2.10:
            return result0, 2.10
        else:
            return result1, 2.10
    if len_s == 20:
        if t_criterium > 2.09:
            return result0, 2.09
        else:
            return result1, 2.09
    if len_s == 21:
        if t_criterium > 2.08:
            return result0, 2.08
        else:
            return result1, 2.08

    if len_s == 22:
        if t_criterium > 2.07:
            return result0, 2.07
        else:
            return result1, 2.07
    if len_s == 23:
        if t_criterium > 2.07:
            return result0, 2.07
        else:
            return result1, 2.07
    if len_s == 24:
        if t_criterium > 2.06:
            return result0, 2.06
        else:
            return result1, 2.06
    if len_s == 25:
        if t_criterium > 2.06:
            return result0, 2.06
        else:
            return result1, 2.06
    if len_s == 26:
        if t_criterium > 2.05:
            return result0, 2.05
        else:
            return result1, 2.05
    if len_s == 27:
        if t_criterium > 2.05:
            return result0, 2.05
        else:
            return result1, 2.05
    if len_s == 28:
        if t_criterium > 2.05:
            return result0, 2.05
        else:
            return result1, 2.05
    if len_s == 29:
        if t_criterium > 2.04:
            return result0, 2.04
        else:
            return result1, 2.04
    if len_s == 30:
        if t_criterium > 2.04:
            return result0, 2.04
        else:
            return result1, 2.04