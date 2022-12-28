task = '''
Введите корни уравнения через пробел $[a]x^2 + [b]x + [c] = 0$.
'''

ranges = dict(
    a=range(1, 3),
    b=range(-10, 10),
    c=range(-10, 10),
)


# если возвращает None, то не добавляет в тесты
def solve_square(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return []
    elif d == 0:
        x = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        return [x]
    else:
        x1 = (-b + ((b ** 2) - (4 * (a * c))) ** 0.5) / (2 * a)
        x2 = (-b - ((b ** 2) - (4 * (a * c))) ** 0.5) / (2 * a)
        return [x1, x2]
    return []

def solution(a, b, c):
    roots = solve_square(a, b, c)
    if roots and [int(i) for i in roots] == roots:
        return roots

if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, solution, amount=100)

