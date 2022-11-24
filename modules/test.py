import math
test = r'$\sqrt{[x]}\cdot\sqrt{[y]}$'

def solution(x, y):
    answer = x ** 0.5 * y ** 0.5
    if round(answer) == answer:
        return answer


if __name__ == '__main__':
    import GENERATOR

    GENERATOR.generate_test(test, {}, solution)
