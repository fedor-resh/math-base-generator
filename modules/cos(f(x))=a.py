import math
from square_equation import solution as solve_square
task = r'$\cos{\pi([a]x^{2} + [b]x + [c])} = [e]$'

ranges = dict(
    e=[-1, -0.5, 0, 0.5, 1],
    a=range(-3, 3),
    b=range(-5, 5),
    c=range(-20, 20),
)

def arccos(x):
    return math.acos(x) / math.pi

def solution(a, b, c, e):
    left = arccos(e)
    # solve quadratic equation
    c -= left + 10
    roots_array = []
    for i in range(0, 11, 2):
        roots = solve_square(a, b, round(c + i, 4))
        if roots:
            roots_array.extend(roots)
    return min([i for i in roots_array if i > 0])


if __name__ == '__main__':
    import GENERATOR

    GENERATOR.generate_test(task, ranges, solution)
