from templates import get_integer_roots, latex_to_function
from GENERATOR import generate_test

latex = r'$\sqrt{[a]x^{2}+[b]x+[c]} \cdot ([d]x^{2}+[e]x+[f]) > 0$'

foo = latex_to_function(latex)
task = r'Найдите максимальное целое решение' + latex


def solution(**k):
    roots = get_integer_roots(foo(**k), RANGE=range(-100, 100))
    if max(roots) != 99:
        return max(roots)


generate_test(task, {}, solution, add=True)
task = r'Найдите количество целых решений ' + latex


def solution(**k):
    roots = get_integer_roots(foo(**k), RANGE=range(-100, 100))
    if roots[0] != -100 and roots[-1] != 99 and sum(roots) != 0:
        return len(roots)


generate_test(task, {}, solution, add=True)

task = r'Найдите сумму целых решений ' + latex


def solution(**k):
    roots = get_integer_roots(foo(**k), RANGE=range(-100, 100))
    if roots[0] != -100 and roots[-1] != 99 and sum(roots) != 0 and sum(roots) < 100:
        return sum(roots)


generate_test(task, {}, solution, add=True)
