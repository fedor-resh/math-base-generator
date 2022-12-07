from templates import get_solution_of_inequality, get_roots_of_polynomial

task = r'$\cos{\pi * ([a]x^{2} + [b]x + [c])} = [e]$'

if __name__ == '__main__':
    from GENERATOR import generate_test
    from templates import get_solution
    generate_test(task, {'e': [-1, -0.5, 0, 0.5, 1]})
