from random import choice

from latex_to_python import latex_to_python

task = r'''
:: task
:: Решите уравнение $\frac{[a]}{[b]}\cdot\sqrt{[c]}+\frac{[d]}{[e]}\cdot\sqrt{[f]}$. При необходимости выводить с чточностью вплоть до сотых(1,0 -> 1; 1,2 -> 1,2; 1,23 -> 1,23; 1,234-> 1,23).
'''

ranges = dict(
    a=range(2, 15),
    b=range(2, 15),
    d=range(2, 15),
    e=range(2, 15),
    c=list(map(lambda x: x ** 2 / choice([1, 100]), range(2, 20))),
    f=list(map(lambda x: x ** 2 / choice([1, 100]), range(2, 20))),
)


def solution(a, b, c, d, e, f):
    answer = eval(latex_to_python(r'\frac{[a]}{[b]}\cdot\sqrt{[c]}+\frac{[d]}{[e]}\cdot\sqrt{[f]}'))
    if int(answer) == answer:
        return int(answer)
