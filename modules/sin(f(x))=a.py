import math
from solve_square import solution as solve_square
task = r'$\cos{\pi([a]x^{2} + [b]x + [c])} = [e]$'

ranges = dict(
    e=[-1, -0.5, 0, 0.5, 1],
)

def arccos(x):
    return math.acos(x) / math.pi

def solution(a, b, c, e):
    left = arccos(e)
    # solve quadratic equation
    c -= left
    roots = solve_square(a, b, c)
    if roots:
        return sorted(roots)[0]


if __name__ == '__main__':
    import GENERATOR

    GENERATOR.generate_test(task, ranges, solution)
