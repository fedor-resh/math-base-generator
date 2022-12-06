def get_integer_roots(func, RANGE=range(-10, 10), nulls=0):
    roots = []
    for x in RANGE:
        if func(x):
            roots.append(x)
            nulls -= 1
    if nulls <= 0:
        return roots


def get_roots_of_polynomial(a=None, b=None, c=None, d=None):
    '''
    solve linear equation 2 args
    solve square equation 3 args
    solve cubic equation 4 args
    :return: list of roots
    '''
    coefficients = list(filter(lambda x: x is not None, [a, b, c, d]))
    if len(coefficients) == 2:
        return [-b / a]
    if len(coefficients) == 3:
        D = b ** 2 - 4 * a * c
        if D < 0:
            return []
        elif D == 0:
            return [-b / (2 * a)]
        else:
            return [(-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)]
    if len(coefficients) == 4:
        import math
        roots = []
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
        try:
            roots = [round(root, 6) for root in roots]
        except:
            return roots
        return roots


def get_solution_of_inequality(func, RANGE=range(-10, 10), nulls=0):
    '''
    :param func: inequality function
    :param RANGE: range of enumeration
    :return: string of solution for example '(1;2)u[3;+inf)'
    '''
    answer = ''
    prev = None
    for x in RANGE:
        try:
            analize = [func(x - 0.000001), func(x), func(x + 0.000001)]
            if not type(analize[0]) == bool:
                print('Error: function must return bool')
                return
        except ZeroDivisionError:
            analize = [func(x - 0.000001), False, func(x + 0.000001)]

        if analize[1] and x == RANGE[-1]:
            answer += '+inf)u'
        if analize[1] and x == RANGE[0]:
            answer += '(-inf,'
        if (not prev is None) and analize[0] != prev:
            return
        prev = analize[2]
        if all(analize) or not any(analize):
            continue
        nulls -= 1
        if analize[1] == analize[2] == True:
            answer += f'[{x};'
        elif analize[0] == analize[1] == True:
            answer += f'{x}]u'
        elif analize[0] == analize[2] == True:
            answer += f'{x})u({x};'
        elif analize[0]:
            answer += f'{x})u'
        elif analize[2]:
            answer += f'({x};'
        elif analize[1]:
            answer += f'{{{x}}}u'
        else:
            print('Error')
    if nulls <= 0 and answer[-1] == 'u':
        return answer[:-1]


def get_solution(latex, RANGE=range(-10, 10), nulls=0):
    from latex import latex_to_python
    pythonn = latex_to_python(latex)
    if '>=' in pythonn:
        f = get_solution_of_inequality
    else:
        pythonn = pythonn.replace('=', '==')
        f = get_integer_roots

    def solution(**kwargs):
        python = pythonn
        for key, value in kwargs.items():
            python = python.replace(key, str(value))
        return f(lambda x: eval(python), RANGE=RANGE, nulls=nulls)
    return solution


if __name__ == '__main__':
    def f(**kwargs):
        print(kwargs)


    f(a=1, b=2)
