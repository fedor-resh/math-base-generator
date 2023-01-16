from random import choice
from math import log
from latex import latex_to_python, python_to_latex, render_latex

# from latex import latex_to_python

task = r'''
Найдите значение выражения $\frac{\log_{[a]}{\log_{[b]}{[c]^{[d]}}}}{\log^{[e]}_{[f]}{[g]^{[h]}}}$
'''
task = r'''
Найдите значение выражения $\frac{1}{[a]}*(\log_{2}{([c]x-[d])}^{[e]})^{[f]}=\frac{\log_{10}{([h]-[i]x)}}{\log_{10}{[k]}}*[l]^{[m]*\log_{2}{\sqrt{[o]}}}$
'''

ranges = dict(
)


if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges)
