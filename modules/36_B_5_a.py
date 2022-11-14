from random import choice

from latex_to_python import latex_to_python

task = r'''
:: Решите уравнение $-\sqrt{[a]^{[b]}\cdot[c]^{[d]}}$. При необходимости выводить с чточностью вплоть до сотых(1,0 -> 1; 1,2 -> 1,2; 1,23 -> 1,23; 1,234-> 1,23).
'''

ranges = dict(
    a=range(-8, 8),
    b=list(2 * i for i in range(2, 4)),
    c=range(-8, 8),
    d=list(2 * i for i in range(2, 4)),
)


def solution(a, b, c, d):
    answer = eval(latex_to_python(r'-\sqrt{[a]^{[b]}\cdot[c]^{[d]}}'))
    if int(answer) == answer:
        return int(answer)
