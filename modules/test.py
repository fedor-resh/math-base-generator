import math

task = r'$\frac{[a]x^{2} + [b]x + [c]}{[d]x + [e]} = [f]$'


def solution(a, b, c, d, e, f):
    b += d * f
    c += e * f
    D = b ** 2 - 4 * a * c
    if D < 0:
        return
    if D == 0:
        x = -b / (2 * a)
        if int(x) == x and 0 != d * x + e:
            return int(x)
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        x1 = x1 if d * x1 + e else 0
        x2 = x2 if d * x2 + e else 0
        if int(x1) == x1 and int(x2) == x2 and x1 != x2:
            return sum(x1, x2)

if __name__ == '__main__':
    import GENERATOR

    GENERATOR.generate_test(task, {}, solution)
