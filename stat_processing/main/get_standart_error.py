import math

def resurn_se(stroke_param, average):
    interlist = []
    for i in stroke_param:
        interlist.append((i - average) ** 2)

    se = math.sqrt(sum(interlist) / (len(stroke_param) * (len(stroke_param) - 1)))

    return se