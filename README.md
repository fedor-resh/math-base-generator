# Пример файла для работы компилятора
```python
# Текст задачи с переменными в виде [переменная]

task = r'Решите уравнение $\frac{[a]}{[b]}$.'


# Переменным присваиваются списки значений которые они могут принимать 
# по умолчанию range(1, 10)

ranges = dict(
    a=range(1, 3),
    b=range(-10, 10),
)


# Решение задачи


def solution(a, b):
    answer = a / b
    # если функция возвращает None или ничего, то пример пропускается
    if round(answer, 2) == answer:
        # генерить если в ответе не больше 2 знаков после запятой
        return answer
    elif answer > 10:
        # можно регулировать сложность с помощью величины
        return answer
    
# для запуска в файле

if __name__ == '__main__':
    from GENERATOR import generate_test
    generate_test(task, ranges, solution)
```