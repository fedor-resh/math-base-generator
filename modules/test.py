import math

test = r'$\sqrt{[x]}\cdot\sqrt{[y]}$'


def solution(x, y):
    answer = x ** 0.5 * y ** 0.5
    if round(answer, 6) == int(answer):
        return int(answer)


ranges = dict(
    x=range(2, 20),
    y=range(2, 20),
)

if __name__ == '__main__':
    import GENERATOR
    GENERATOR.generate_test(test, ranges, solution)
