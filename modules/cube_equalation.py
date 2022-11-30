import math

task = r'Найдите сумму корней $[a]x^{3} + [b]x^{2} + [c]x + [d] = 0$'

ranges = dict(
    a=range(-3, 3),
    b=range(-10, 10),
    c=range(-10, 10),
    d=range(-10, 10),
)


def NOD(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(a, b, c, d):
    if a == 0 or b == 0 or c == 0 or d == 0 or NOD(a, NOD(b, NOD(c, d))) == 1:
        return
    roots = []
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    if p == 0:
        if q == 0:
            roots.append(-b / (3 * a))
        else:
            u = q ** 0.5
            roots.append(2 * u - b / (3 * a))
            roots.append(-u - b / (3 * a))
    else:
        if q == 0:
            roots.append((2 * p) ** 0.5 - b / (3 * a))
            roots.append(-(2 * p) ** 0.5 - b / (3 * a))
        else:
            D = q ** 2 / 4 + p ** 3 / 27
            if D > 0:
                u = (-q / 2 + D ** 0.5) ** (1 / 3)
                v = (-q / 2 - D ** 0.5) ** (1 / 3)
                roots.append(u + v - b / (3 * a))
            else:
                u = 2 * (q / 2) ** 0.5
                v = math.acos(-q / (2 * (q / 2) ** 1.5))
                roots.append(u * math.cos(v / 3) - b / (3 * a))
                roots.append(u * math.cos((v + 2 * math.pi) / 3) - b / (3 * a))
                roots.append(u * math.cos((v + 4 * math.pi) / 3) - b / (3 * a))
    if len(roots) == 3 and all([root % 1 == 0 for root in roots]):
        return sum(roots)


if __name__ == '__main__':
    import GENERATOR

    GENERATOR.generate_test(task, ranges, solution, amount=10)
