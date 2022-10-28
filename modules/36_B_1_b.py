task = r'''
:: Решите уравнение $\left(-\frac{\sqrt{[a]}}{[b]}\right)^{2}$. При необходимости выводить с чточностью вплоть до сотых(1,0 -> 1; 1,2 -> 1,2; 1,23 -> 1,23; 1,234-> 1,23).
'''

ranges = dict(
    a=list(map(lambda x: x ** 2, range(2, 20))),
    b=range(2, 20),
)


# если возвращает None, то не добавляет в тесты
def solution(a, b):
    answer = (a ** 0.5 / b) ** 2
    if int(answer) == answer:
        return int(answer)
    return

