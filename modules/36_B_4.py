from GENERATOR import generate_test

test_36_B = dict(
    task_mask='''
::Укажите количество целых чисел, расположенные на координатной прямой между точками $-(sqrt{[a]})^{2}$ и $-sqrt{[a]}$.
''',
    ranges=dict(a=range(3, 11, 2)),
    solution=lambda a: int((a ** 0.5) ** 2 - a ** 0.5) if (a ** 0.5) ** 2 - a ** 0.5 else None
)

if __name__ == '__main__':
    generate_test(**test_36_B, amount=100, type_of_test='simple')
