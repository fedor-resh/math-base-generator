# task = r'$[a]x^3+[b]x^2+[c]x+[d]<0$'
#
# ranges = dict(
#     x1=range(-10, 10),
#     x2=range(-10, 10),
#     x3=range(-10, 10),
#     a=range(-5, 4),
#     b=lambda x1, x2, x3, a: (x1 + x2 + x3) * a,
#     c=lambda x1, x2, x3, a: (x1 * x2 + x2 * x3 + x1 * x3) * a,
#     d=lambda x1, x2, x3, a: (x1 * x2 * x3) * a,
# )
#
# if __name__ == '__main__':
#     from GENERATOR import generate_test
#     generate_test(task, ranges, amount=1000)

# task = r'$[a]^{[b]*x^{2}+[c]*x+[d]}=[a]^{[e]*x+[f]}$'
#
# ranges = dict(
#     x1=range(-10, 10),
#     x2=range(-10, 10),
#     a=range(-10, 10),
#     b=range(-10, 10),
#     c=lambda x1, x2, a, e: -(x1 + x2) * a + e,
#     d=lambda x1, x2, a, f: (x1 * x2) * a + f,
#     e=range(-10, 10),
#     f=range(-10, 10),
# )
#
# if __name__ == '__main__':
#     from GENERATOR import generate_test
#     generate_test(task, ranges, amount=10)

task = r'$[a]^{[b]*x+[c]}>[a]^{[d]*x+[e]}$'

ranges = dict(
    x1=range(-10, 10),
    a=range(2, 4),
    b=range(0, 10),
    c=range(-10, 10),
    d=lambda b: list(set(range(-10, 10)) - {b}),
    e=lambda x1, b, c, d: -(x1 * b + c) + d,
)

if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, amount=10)