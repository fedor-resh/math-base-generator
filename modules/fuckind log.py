from random import choice
from math import log

# from latex import latex_to_python

task = r'''
Найдите значение выражения  при а = ???.
'''

ranges = dict(
    a=range(2, 15),
    b=range(2, 15),
    c=range(2, 15),
    d=range(2, 15),
)


def solution(a, b, c, d):
    answer = (log(log(b, a), a)) / log(d, a) ** c
    if int(answer) == answer:
        return int(answer)


if __name__ == '__main__':
    from ..GENERATOR import generate_test

    generate_test(task, ranges, solution)