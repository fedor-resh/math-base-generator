# Генератор тестов по математике на портале moodle
## Пример файла для работы компилятора
### генерация выражений и уравнений
```python
# Текст задачи на LaTex с переменными в виде [переменная]
task = r'$\log_{[e]}{(x^2+[b]x+[c])}=[d]$ введите сумму корней'

# Переменные задачи можно задавать в виде словаря
# где ключ - это имя переменной, а значение - это список возможных значений
# также можно задавать переменные в зависимости от других переменных, функцией
ranges = dict(
    default = range(-10, 10),
    x1=range(-10, 10),
    x2=range(-10, 10),
    d=range(1, 3),
    b=lambda x1, x2: x1 + x2,
    c=lambda x1, x2, e, d: x1 * x2 + e**d,
)

if __name__ == '__main__':
    from GENERATOR import generate_test
    generate_test(task, ranges) 
    # автоматически генерит выражения 
    # и уравнения с суммой корней в качестве ответа

```

### генерация неравенств
```python
task = r'$\log_{[e]}{(x^2+[b]x+[c])}>[d]$'
ranges = dict(
    x1=range(-10, 10),
    x2=range(-10, 10),
    d=lambda b: range(1, 3),
    b=lambda x1, x2: x1 + x2,
    c=lambda x1, x2, e, d: x1 * x2 + e**d,
)

if __name__ == '__main__':
    from templates import generate_inequality_test
    generate_inequality_test(task, ranges, nulls=2)
    # nulls - максимальное количество нулей в уравнении из неравенства
    # если не устанавливать, могут теряться корни
```

## пример своего решения
```python
task = r'решите выражение $\frac{[a]}{[b]}$'
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

if __name__ == '__main__':
    from GENERATOR import generate_test
    generate_test(task, ..., solution)
```
