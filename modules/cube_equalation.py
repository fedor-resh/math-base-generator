import math

task = r'Найдите сумму корней $[a]x^{3} + [b]x^{2} + [c]x + [d] = 0$'

ranges = dict(
    a=range(-3, 3),
    b=set(range(-5, 5)) - set(range(-3, 3)),
    c=set(range(-20, 20)) - set(range(-3, 3)),
    d=set(range(-100, 100)) - set(range(-3, 3)),
)


def NOD(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(a, b, c, d):
    # if NOD(a, NOD(b, NOD(c, d))) != 1:
    #     return
    roots = []

    # solve cubic equation
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    D = q ** 2 / 4 + p ** 3 / 27
    if D > 0:
        u = (-q / 2 + math.sqrt(D)) ** (1 / 3)
        v = (-q / 2 - math.sqrt(D)) ** (1 / 3)
        roots.append(u + v - b / (3 * a))
    elif D == 0:
        u = (-q / 2) ** (1 / 3)
        roots.append(2 * u - b / (3 * a))
        roots.append(-u - b / (3 * a))
    else:
        u = 2 * math.sqrt(-p / 3)
        v = math.acos(-math.sqrt(-27 / p ** 3) * q / 2) / 3
        roots.append(u * math.cos(v) - b / (3 * a))
        roots.append(-u * math.cos(v + math.pi / 3) - b / (3 * a))
        roots.append(-u * math.cos(v - math.pi / 3) - b / (3 * a))
    roots = [round(root, 6) for root in roots]
    if len(set(roots)) == 3 and all([root % 1 == 0 for root in roots]):
        return roots


if __name__ == '__main__':
    import GENERATOR
    GENERATOR.generate_test(task, ranges, solution, amount=20)
