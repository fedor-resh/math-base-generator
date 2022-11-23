task = r'''
Решите уравнение $\left(-\frac{\sqrt{[a]}}{[b]}\right)^{2}$.
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

if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, solution)


