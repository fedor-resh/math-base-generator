from random import choice

from latex_to_python import latex_to_python

task = r'''
Решите уравнение $\frac{[a]}{[b]}\cdot\sqrt{[c]}+\frac{[d]}{[e]}\cdot\sqrt{[f]}$.
'''

ranges = dict(
    a=range(2, 15),
    b=range(2, 15),
    d=range(2, 15),
    e=range(2, 15),
    c=list(map(lambda x: x ** 2, range(2, 20))),
    f=list(map(lambda x: x ** 2, range(2, 20))),
)


def solution(a, b, c, d, e, f):
    answer = eval(latex_to_python(r'\frac{[a]}{[b]}\cdot\sqrt{[c]}+\frac{[d]}{[e]}\cdot\sqrt{[f]}'))
    if int(answer) == answer:
        return int(answer)

if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, solution)