task = r'''
Решите уравнение $\sqrt{[a]\cdot\frac{[b]}{[c]}\cdot\frac{[d]}{[e]}}-\sqrt{[f]}$.
'''

ranges = dict(
    a=range(2, 20),
    b=range(2, 20),
    c=[i ** 2 for i in range(2, 20)],
    d=range(2, 20),
    e=[i ** 2 for i in range(2, 20)],
    f=[i ** 2 for i in range(2, 20)],
)


# если возвращает None, то не добавляет в тесты
def solution(a, b, c, d, e, f):
    answer = (a * (b/c) * (d/e)) ** 0.5 - f ** 0.5
    if int(answer) == answer:
        return int(answer)
    return

if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, solution)