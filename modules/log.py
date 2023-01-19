from random import choice
from math import log
from latex import latex_to_python, python_to_latex, render_latex

# from latex import latex_to_python

task = r'''
Найдите значение выражения $\frac{1}{[a]}*(\log_{2}{([c]-[d])}^{[e]})^{[f]}-\frac{\log_{10}{([h]-[i])}}{\log_{10}{[k]}}*[l]^{[m]*\log_{2}{\sqrt{[o]}}}$
'''

ranges = dict(
    a=range(2, 10),
    b=range(2, 10),
    c=range(2, 10),
    d=range(2, 10),
    e=range(2, 10),
    f=range(2, 10),
    g=range(2, 10),
    h=range(2, 10),
    i=range(2, 10),
    k=range(2, 10),
    l=range(2, 10),
    m=range(2, 10),
    o=range(2, 10),

)


if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges)
