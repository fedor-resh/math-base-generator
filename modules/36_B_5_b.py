from random import choice

from latex import latex_to_python

task = r'''
Решите уравнение $-\sqrt{[a]^{[b]}\cdot[c]^{[d]}}$.
'''

ranges = dict(
    a=range(2, 8),
    b=list(2 * i for i in range(2, 4)),
    c=range(2, 8),
    d=list(2 * i for i in range(2, 4)),
)


def solution(a, b, c, d):
    answer = eval(latex_to_python(r'-\sqrt{[a]^{[b]}\cdot[c]^{[d]}}'))
    if int(answer) == answer:
        return int(answer)
