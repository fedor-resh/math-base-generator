from random import choice
from math import log

# from latex import latex_to_python

task = r'''
Найдите значение выражения $\frac{\log_{[a]} \log_{[b]}[c]^{[d]}}{\log^{[e]}_{[f]}[g]^{[h]}}$
'''

ranges = dict(

)


def solution(a, b, c, d, e, f, g, h):
    answer = (log(log(c ** d, b), a)) / log(g ** h, f) ** e
    if int(answer) == round(answer, 8) and -1000 < answer < 1000:
        return int(answer)


if __name__ == '__main__':
    import sys

    sys.path.insert(1, '../../')
    from GENERATOR import generate_test

    generate_test(task, ranges, solution)
