task = '''
:: Укажите количество целых чисел, расположенные на координатной прямой между точками $-(sqrt{[a]})^{2}$ и $-sqrt{[a]}$.
'''
ranges = dict(a=range(3, 11, 2))


def solution(a):
    return int((a ** 0.5) ** 2 - a ** 0.5)
