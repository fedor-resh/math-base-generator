task = r'''
:: Решите уравнение $\sqrt{[a]\cdot\frac{[b]}{[c]}\cdot\frac{[d]}{[e]}}-\sqrt{[f]}$. При необходимости выводить с чточностью вплоть до сотых(1,0 -> 1; 1,2 -> 1,2; 1,23 -> 1,23; 1,234-> 1,23).
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

