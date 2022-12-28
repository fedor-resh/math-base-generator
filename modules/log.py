from random import choice
from math import log

# from latex import latex_to_python

task = r'''
Найдите значение выражения $\frac{\log_{[a]} \log_{[a]}[a]^[b]}{\log^{[c]}_{[a]}[a]^{[d]}}$
'''

ranges = {}


def solution(a, b, c, d):
    answer = (log(log(a ** b, a), a)) / log(a ** d, a) ** c
    if int(answer) == round(answer, 3) and  -100 < answer < 100:
        return int(answer)


if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, solution)