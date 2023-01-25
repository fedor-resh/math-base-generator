from random import choice
from math import log

task = r'Решите уравнение $[a]x^3+[b]x^2+[c]x+[d]=0$'

ranges = dict(
    x1=range(-100, 100),
    x2=range(-100, 100),
    x3=range(-100, 100),
    a=lambda x1, x2, x3: 1,
    b=lambda x1, x2, x3: -(x1 + x2 + x3),
    c=lambda x1, x2, x3: x1 * x2 + x2 * x3 + x1 * x3,
    d=lambda x1, x2, x3: -x1 * x2 * x3,
)

if __name__ == '__main__':
    from GENERATOR import generate_test
    from templates import get_solution
    generate_test(task, ranges, get_solution(task, nulls=3))
