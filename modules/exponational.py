from templates import get_integer_roots, latex_to_function, get_answer_of_inequality, get_solution
task = r'Найдите значение выражения $[a]^{\sqrt{[b]}+[c]} \cdot [g]^{[d]+\sqrt{[e]}}$'

ranges = {
    'a': range(2, 10),
    'g': range(2, 10),
}

# def solution(a,b,c,d,e,g):
#     answer = eval(latex_to_python(task))
#     if int(answer) == round(answer, 6) and -100 < answer < 100:
#         return int(answer)

task = r'Найдите значение выражения $[e]^{\sqrt{[f]}}*\sqrt{[a]^{[b]}*[c]^{\frac{1}{[d]}}}$'

ranges = {
    'a': range(2, 10),
    'g': range(2, 10),
    'e': range(2, 10),
}

if __name__ == '__main__':
    from GENERATOR import generate_test
    import latex
    print(latex.latex_to_python(task))
    generate_test(task, ranges, get_solution(task))