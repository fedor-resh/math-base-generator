
#task = r'$\sqrt{[a]x^{2}+[b]x+[c]}*(x+[b])^{2}=0$'
#task = r'$\sqrt{\frac{x+[a]}{[a]-x}}+[b]*\sqrt{\frac{[a]-x}{x+[a]}}>[c]$'
task = r'$\sqrt{[a]x^{2}+[b]}>[c]$'

ranges = dict(
    # default=range(-100, 100)
    x1=range(-10, 10),
    a=range(-10, 10),
    b=range(-10, 10),
    c=lambda a,b,x1:  (a*x1**2+b)**2
    # d=lambda b: list(set(range(-10, 10)) - {b}),
    # e=lambda x1, b, c, d: -(x1 * b + c) + d,
)

if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, amount=1000)