# Пример файла для работы компилятора

## Текст задачи с переменными в виде [переменная]

```python
task = r'Решите уравнение $\frac{[a]}{[b]}$.'
```

## Переменным присваиваются списки значений которые они могут принимать

```python
ranges = dict(
    a=range(1, 3),
    b=range(-10, 10),
)
```

## Решение задачи

```python
def solution(a, b):
    if round(a / b, 2) == a / b: 
        # генерить если в ответе не больше 2 знаков после запятой
        return a / b
```

## для запуска в файле

```python
if __name__ == '__main__':
    from GENERATOR import generate_test
    generate_test(test, ranges, solution)
```