from random import choice
from math import log

# from latex import latex_to_python

task = r'''
Найдите значение выражения $\frac{\log_{[a]} \log_{[b]}[c]^{[d]}}{\log^{[e]}_{[f]}[g]^{[h]}}$
'''

ranges = dict(
    a=range(-16, 17),
    b=range(-16, 17),
    c=range(2, 17),
    d=range(-16, 17),
    e=range(-16, 17),
    f=range(-16, 17),
    g=range(2, 17),
    h=range(-16, 17),
)


def solution(a, b, c, d, e, f, g, h):
    answer = (log(log(c ** d, b), a)) / log(g ** h, f) ** e
    if int(answer) == round(answer, 8) and -1000 < answer < 1000:
        return int(answer)


if __name__ == '__main__':
    import sys

    sys.path.insert(1, '../')
    from GENERATOR import generate_test

    generate_test(task, ranges, solution)
