import math
from latex import latex_to_python
task = r'Найдите минимальный натуральный корень $\cos{(\pi([a]x^{2} + [b]x + \frac{[c]}{3}))} = [e]$'
def arccos(x):
    return math.acos(x) / math.pi

ranges = dict(
    x1=range(2, 10),
    x2=range(2, 10),
    e=[r'\frac{1}{2}', r'\frac{\sqrt{2}}{2}', r'-\frac{1}{2}', r'-\frac{\sqrt{2}}{2}', r'\frac{sqrt{3}}{2}', r'-\frac{sqrt{3}}{2}'],
    f=lambda e: eval(latex_to_python(e)),
    a=range(1, 3),
    b=lambda x1, x2, a: (x1 + x2) * a,
    rand=[i/24 for i in range(1, 24)],
    c=lambda x1, x2, rand, a: (x1 * x2+ rand)*a*3,
)


def solution(x1, x2, a, b, c, f, e):
    for i in range(1, 10):
        if round(math.cos(math.pi * (a * i**2 + b * i + c)),5) == round(f, 5):
            return i


if __name__ == '__main__':
    import GENERATOR

    GENERATOR.generate_test(task, ranges, solution)
