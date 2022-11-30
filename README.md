# Генератор тестов по математике на портале moodle
## Пример файла для работы компилятора
```python
# Текст задачи на LaTex с переменными в виде [переменная]

task = r'Решите уравнение $\frac{[a]}{[b]}$.'


# Переменным присваиваются списки значений которые они могут принимать 

# по умолчанию range(2, 11)
ranges = dict(
    a=range(1, 3),
    b=range(-10, 10),
)


# Решение задачи


def solution(a, b):
    answer = a / b
    # примеры обработки ответа:
    if round(answer, 2) == answer:
        # генерить если в ответе не больше 2 знаков после запятой
        return answer
    elif answer > 10:
        # можно регулировать сложность с помощью величины
        return answer
    elif round(answer, 6) == int(answer):
        # генерить если ответ почти не отличается от целого (погрешность)
        return answer
    # если ничего не вернулось, то пример пропускается
    return None
    
# для запуска в файле

if __name__ == '__main__':
    from GENERATOR import generate_test
    generate_test(task, ranges, solution)
```
