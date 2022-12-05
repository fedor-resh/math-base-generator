from templates import get_solution_of_inequality

task = r'[a]x^3 + [b]x^2 + [c]x + [d] > 0'
ranges = dict(
    a=range(-3, 3),
    b=range(-5, 5),
    c=range(-20, 20),
    d=range(-20, 20),
)

def solution(a, b, c, d):
    from templates import get_roots_of_polynomial
    if len(get_roots_of_polynomial(a, b, c, d)) == 3:
        return get_solution_of_inequality(lambda x: a * x ** 3 + b * x ** 2 + c * x + d >= 0)

if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, solution)

