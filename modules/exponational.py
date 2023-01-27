from templates import get_integer_roots, latex_to_function, get_answer_of_inequality, get_solution

# task = r'Найдите значение выражения $[a]^{\sqrt{[b]}+[c]} \cdot [g]^{[d]+\sqrt{[e]}}$'

# ranges = {
#     'a': range(2, 10),
#     'g': range(2, 10),
# }

# def solution(a,b,c,d,e,g):
#     answer = eval(latex_to_python(task))
#     if int(answer) == round(answer, 6) and -100 < answer < 100:
#         return int(answer)

task = r'Найди значение выражения ' \
       r'$\frac{1}{[a]}*\left(\log_{2}{([b]x+[c])}^{[d]}\right)^{[e]}' \
       r'=\frac{\log_{[f]}{([g]+[h]x)}}{\log_{[f]}{2}}*[k]^{2*\log_{[k]}{\sqrt{[m]}}}$'

ranges = dict(
    s=[i**2 for i in range(2, 5)],
    x1=range(-10, 10),
    b=range(-10, 10),
    c=lambda x1, b, s: s - x1 * b,
    f=range(2, 10),
    j=range(2, 4),
    s1=lambda j: [i ** j for i in range(2, 5)],
    h=range(-10, 10),
    g=lambda x1, h, s1: s1 - x1 * h,
    e=range(2, 4),
)
if __name__ == '__main__':
    from GENERATOR import generate_test
    generate_test(task, ranges, get_solution(task))
