
#task = r'$\sqrt{[a]x^{2}+[b]x+[c]}*(x+[b])^{2}=0$'
#task = r'$\sqrt{\frac{x+[a]}{[a]-x}}+[b]*\sqrt{\frac{[a]-x}{x+[a]}}>[c]$'
task = r'$x*\sqrt{[a]x+[b]}=[c]$'

ranges = dict(
    # default=range(-100, 100)
    x1=range(-10, 10),
    a=range(-10, 10),
    b=range(-100, 100),
    c=lambda a,b,x1:  (a*x1+b)**2 if (a*x1+b)>0 else -1
)

if __name__ == '__main__':
    from GENERATOR import generate_test

    generate_test(task, ranges, amount=10)