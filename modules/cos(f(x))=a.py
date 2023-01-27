import math
from latex import latex_to_python
task = r'Найдите минимальный натуральный корень $\cos{(\pi([a]x^{2} + [b]x + [c]))} = -\frac{\sqrt{2}}{2}$'
def arccos(x):
    return math.acos(x) / math.pi

ranges = dict(
    x1=range(-10, 10),
    x2=range(-10, 10),
    a=range(1, 4),
    b=lambda x1, x2, a: (x1 + x2) * a,
    rand=[i/12 for i in range(1, 48)],
    c=lambda x1, x2, rand, a: (x1 * x2 + rand) * 3,
)


def solution(x1, x2, a, b, c):
    for i in range(1, 10):
        if math.cos(math.pi * (a * i**2 + b * i + c)) == -math.sqrt(2) / 2:
            return i


if __name__ == '__main__':
    import GENERATOR

    GENERATOR.generate_test(task, ranges, solution, amount=10)
