task = r'Найдите количество целых корней $[a]x^2 + [b]x + [c] > 0$.'
from latex import latex_to_python

ranges = dict(
    a=range(-3, 3),
    b=range(-5, 5),
    c=range(-20, 20),
)


def solution(a, b, c):
    count = 0
    for x in range(-100, 100):
        if eval(latex_to_python('[a]x^2 + [b]x + [c] > 0')):
            count += 1
    if 100 > count > 1:
        return count


if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, solution, amount=20)
