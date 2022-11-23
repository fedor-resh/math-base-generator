from random import choice

from latex_to_python import latex_to_python

task = r'''
Решите уравнение $[char]\sqrt{[a]^{[b]}\cdot[c]^{[d]}}$
'''

ranges = dict(
    a=[-4, -3, -2, 2, 3, 4],
    b=list(2 * i for i in range(2, 3)),
    c=[-4, -3, -2, 2, 3, 4],
    d=list(2 * i for i in range(2, 3)),
    char=['-', ''],
)


def solution(a, b, c, d, char):
    answer = ((a ** b) * (c ** d)) ** 0.5 * (-1 if char == '-' else 1)
    if int(answer) == answer:
        return int(answer)

if __name__ == '__main__':
    import sympy

    s = "1+2**(x+y)"
    print(sympy.latex(sympy.simplify(s)))  # prints '$1 + {2}^{x + y}$'
