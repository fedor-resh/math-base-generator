import math
from latex import latex_to_python
from utils import get_params_from_task
import re
def get_integer_roots(func, RANGE=range(-10, 10), nulls=0):
    roots = []
    for x in RANGE:
        try:
            if func(x):
                roots.append(x)
                nulls -= 1
        except:
            pass
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


def get_answer_of_inequality(func, RANGE=range(-10, 10), nulls=0):
    prev = None
    for x in RANGE:
        try:
            analize = [func(x - 0.000001), func(x), func(x + 0.000001)]
            if not type(analize[0]) == bool:
                print('Error: function must return bool')
                return
        except:
            analize = [func(x - 0.000001), False, func(x + 0.000001)]
        if (not prev is None) and analize[0] != prev:
            return
        prev = analize[2]
        if all(analize) or not any(analize):
            continue
        nulls -= 1
    if nulls <= 0 and not prev:
        return True
def latex_to_function(latex):
    params = get_params_from_task(latex)
    python = latex_to_python(latex)
    left, mid, right = re.split(r'(<=|>=|<|>|==)', python)
    python = f'round({left}, 6){mid}round({right}, 6)'
    print('lambda ' + ','.join(params) + ':' + 'lambda x:' + python)
    foo = eval('lambda ' + ','.join(params) + ':' + 'lambda x:' + python)
    return foo


def get_solution(latex, **rest):
    python = latex_to_python(latex)
    params = get_params_from_task(latex)
    print(python)
    if 'x' not in python:
        print(params)
        return eval(f'lambda {",".join(params)}: '
                    f'int((answer:={python}))==answer'
                    f' and -100 < answer < 100  and not -1e-05 < answer < 1e-05 and answer')
    foo = latex_to_function(latex)
    return lambda **kwargs: sum(get_integer_roots(foo(**kwargs), **rest))





if __name__ == '__main__':
    def f(**kwargs):
        print(kwargs)


    f(a=1, b=2)
