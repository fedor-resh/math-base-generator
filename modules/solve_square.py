task = '''
:: Вопрос 
:: Решите уравнение $[a]x^2 + [b]x + \sqrt{[c]} = 0$.
'''

ranges = dict(
    a=range(1, 3),
    b=range(-10, 10),
    c=list(map(lambda x: x ** 2, range(1, 10))),
)


# если возвращает None, то не добавляет в тесты
def solution(a, b, c):
    c = int(c ** 0.5)
    d = b ** 2 - 4 * a * c
    if d < 0:
        return ()
    elif d == 0:
        x = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        if x % 1 == 0:
            return int(x)
    else:
        x1 = (-b + ((b ** 2) - (4 * (a * c))) ** 0.5) / (2 * a)
        x2 = (-b - ((b ** 2) - (4 * (a * c))) ** 0.5) / (2 * a)
        if not x1 % 1 and not x2 % 1:
            return int(x1), int(x2)

if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, solution, amount=100)

