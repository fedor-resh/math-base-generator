from templates import get_solution_of_inequality, get_roots_of_polynomial

task = r'$[a]x^{4} + [b]x^{3} + [c]x^{2} + [d]x + [e] = 0$'

if __name__ == '__main__':
    from GENERATOR import generate_test
    from templates import get_solution
    generate_test(task, ranges={'e':range(-100, 100)})
