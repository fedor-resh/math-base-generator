from templates import generate_inequality_test

latex1 = r'$\frac{[a]x^{2}+[b]x+[c]}{[d]x^{2}+[e]x+[f]}>0$'
latex1 = r'$\sqrt{x^{2}+[b]x+[c]}>= [d]x^{2}+[e]x+[f]$'
ranges = dict(
    x1=[i**2 for i in range(-3, 4)],
    x2=[i**2 for i in range(-3, 4)],
    b=lambda x1, x2: x1 + x2,
    c=lambda x1, x2: x1 * x2,
    x3=range(-10, 10),
    x4=range(-10, 10),
    d=range(-5, 5),
    e=lambda x3, x4, d: (x3 + x4) * d,
    # f=lambda x3, x4, d: x3 * x4 * d,
)
generate_inequality_test(latex1, ranges, nulls=2)

# latex = r'$\sqrt{x^{2}+[b]x+[c]} \cdot ([d]x^{2}+[e]x+[f]) > 0$'
#
# ranges = dict(
#     x1=[i**2 for i in range(-3, 4)],
#     x2=[i**2 for i in range(-3, 4)],
#     b=lambda x1, x2: x1 + x2,
#     c=lambda x1, x2: x1 * x2,
#     x3=range(-10, 10),
#     x4=range(-10, 10),
#     d=range(-5, 5),
#     e=lambda x3, x4, d: (x3 + x4) * d,
#     f=lambda x3, x4, d: x3 * x4 * d,
# )
# generate_inequality_test(latex, ranges, nulls=3)



