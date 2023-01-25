from random import choice
from math import log
from latex import latex_to_python, python_to_latex, render_latex

# from latex import latex_to_python

# task = r'''
# Найдите значение выражения $\frac{\log_{[a]}{\log_{[b]}{[c]^{[d]}}}}{\log^{[e]}_{[f]}{[g]^{[h]}}}$
# '''
# task = r'''
# Найдите значение выражения $\frac{1}{[a]}*(\log^{[e]}_{2}{[c]})^{[f]}-\frac{\log_{10}{[h]}}{\log_{10}{[k]}}*[l]^{[m]*\log_{2}{\sqrt{[o]}}}$
# '''
# ranges = dict(
#     a=range(2, 10),
#     b=range(2, 10),
#     c=range(3, 10),
#     d=range(2, 10),
#     e=range(2, 10),
#     f=range(2, 10),
#     g=range(2, 10),
#     h=range(10, 110),
#     i=range(2, 10),
#     k=range(2, 10),
#     l=range(2, 10),
#     m=range(2, 10),
#     o=range(2, 10),
# )
task = r'Решите уравнение $\log_{[a]}{([c]x+[d])} + \log_{[a]}{([e]x+[d])} = \log_{[z]}{([g]x+[h])^{2}}$'

ranges = dict(
    default=range(-100, 100),
    a=range(2, 10),
    c=range(-10, 10),
    e=range(-10, 10),
    z=lambda a: a**2,
)
if __name__ == '__main__':
    from GENERATOR import generate_test
    from templates import get_solution

    generate_test(task, ranges, get_solution(task, nulls=1))

