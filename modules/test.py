from templates import get_solution_of_inequality

task = r'$\sqrt{[a]x^2-[b] x + [c]} \geq \dfrac{[d] x+[e]}{[f]-[l]x}$'
ranges = dict(
    a=range(-10, 10),
    b=range(-10, 10),
    c=range(-10, 10),
    d=range(-10, 10),
    e=range(-10, 10),
    f=range(-10, 10),
    l=range(-10, 10),

)

def solution(a, b, c, d, e, f, l):
    try:
        answer = get_solution_of_inequality(
            lambda x: (a * x ** 2 - b * x + c) ** 0.5 >= (d * x + e) / (f - l * x),
            min_slices=2
        )
    except:
        return
    # print(answer)
    return answer


if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, solution)

