from templates import get_integer_roots, latex_to_function, get_answer_of_inequality, get_solution

task = r'Найдите значение выражения $[a]^{\sqrt{[b]}+[c]} \cdot [g]^{[d]+\sqrt{[e]}}$'

# ranges = {
#     'a': range(2, 10),
#     'g': range(2, 10),
# }

# def solution(a,b,c,d,e,g):
#     answer = eval(latex_to_python(task))
#     if int(answer) == round(answer, 6) and -100 < answer < 100:
#         return int(answer)

task = r'Найдите корни уравнения $\log_8(x+7)=\log_8(2x-15)$'

if __name__ == '__main__':
    from GENERATOR import generate_test
    from utils import replace_numbers_by_variables

    task = replace_numbers_by_variables(task)
    import math

    generate_test(task, {},
                  get_integer_roots(lambda x: math.log(2 * x - 15, 8) == math.log(x + 7, 8), RANGE=range(-10, 10)))
