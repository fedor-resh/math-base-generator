task = r'$[a]x^3+[b]x^2+[c]x+[d]<0$ Введите сумму корней'

ranges = dict(
    x1=range(-10, 10),
    x2=range(-10, 10),
    x3=range(-10, 10),
    a=range(-4, 4),
    b=lambda x1, x2, x3, a: (x1 + x2 + x3) * a,
    c=lambda x1, x2, x3, a: (x1 * x2 + x2 * x3 + x1 * x3) * a,
    d=lambda x1, x2, x3, a: (x1 * x2 * x3) * a,
)

if __name__ == '__main__':
    from GENERATOR import generate_test
    generate_test(task, ranges, amount=1000)