from random import choice

from latex import latex_to_python

task = r'''
Решите уравнение $\frac{2}{3}\cdot\sqrt{4}+\frac{5}{2}\cdot\sqrt{2}$.
'''

if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task)