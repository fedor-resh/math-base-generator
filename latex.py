import re


def latex_to_tex(text):
    parts = text.split('$')
    for i in range(1, len(parts), 2):
        parts[i] = parts[i].replace('*', r'\cdot')
        parts[i] = parts[i].replace(r'\frac', r'\\frac') \
            .replace(r'\sqrt', r'\\sqrt') \
            .replace(r'\left', r'\\left') \
            .replace(r'\right', r'\\right') \
            .replace(r'\cdot', r'\\cdot') \
            .replace('{', r'\{') \
            .replace('}', r'\}')

        parts[i] = r'\(' + parts[i] + r'\)'
    text = ''.join(parts)

    return text



brackets = r'\{([^{}]*(?:(?:\{[^{}]*(?:(?:\{[^{}]*\})*[^{}]*)*[^{}]*\})*[^{}]*)*[^{}]*)\}'

def latex_to_python(latex):
    """:return: python string"""
    if '$' in latex:
        latex = re.match(r'.*\$(.+)\$.*', latex).group(1)
    while '\log' in latex:
        latex = re.sub(r'\\log_'+brackets*2, r'__import__("math").log(\2, \1)', latex)
        latex = re.sub(r'\\log\^'+brackets+'_'+brackets*2, r'__import__("math").log(\3, \2)**\1', latex)

    latex = re.sub(r'\^'+brackets, r'**(\1)', latex)
    latex = re.sub(r'\^(\d+)', r'**\1', latex)
    latex = re.sub(r'\\frac'+brackets*2, r'(\1)/(\2)', latex)
    latex = re.sub(r'\\sqrt'+brackets, r'(\1)**0.5', latex)
    latex = re.sub(r'\[([a-z])\]([a-z])', r'[\1]*\2', latex)
    latex = latex \
        .replace(r'=', '==') \
        .replace('\\cdot', '*') \
        .replace('\\left', '') \
        .replace('\\right', '') \
        .replace('\\geq', '>=') \
        .replace('\\leq', '<=') \
        .replace('$', '') \
        .replace('[', '') \
        .replace(']', '')
    latex = re.sub(r'\\([a-z]+)'+brackets, r'math.\1(\2)', latex)
    latex = re.sub(r'\\([a-z]+)', r'math.\1', latex)

    python_string = latex
    return python_string


def python_to_latex(python):
    """:return: latex string"""
    python = re.sub(r'\((([^()]*(\([^()]*\))*[^()]*)*)\)\*\*0\.5', r'\\sqrt{\1}', python)
    python = re.sub(r'(.)\*\*0\.5', r'\\sqrt{\1}', python)

    python = re.sub(r'(\(.+\)|.)\*\*(\(.+\)|\\[^}]+}|.)', r'\1^{\2}', python)
    python = re.sub(r'([^*])\*([^*])', r'\1 \\cdot \2', python)
    while '/' in python:
        copy = python
        print(python)
        # python = re.sub(r'(\(([^()]*)(\([^()]*\))*([^()]*)\)|([^({})+-]*)({.*})*[^({})+-]*)'
        #                 r'/(\(([^()]*)(\([^()]*\))*([^()]*)\)|([^({})+/-]*)({.*})*[^({})+/-]*)', r'\\frac{\1}{\7}',
        #                 python, count=1)
        python = re.sub(r'\((([^()]*(\([^()]*\))*[^()]*)*)\)'
                        r'/\((([^()]*(\([^()]*\))*[^()]*)*)\)',
                        r'\\frac{\1}{\4}', python)
        python = re.sub(r'\(([^()]*)'
                        r'/([^()]*)\)',
                        r'\\frac{\1}{\2}', python)

        if copy == python:
            print('ERROR')
            break
    print('exit' + python)
    latex = python.replace('(', r'\left(').replace(')', r'\right)')
    render_latex(latex)
    return latex


def render_latex(tex):
    import re
    print('render_latex')
    print(tex)
    try:
        tex = re.match(r'.*\$(.+)\$.*', tex).group(1)
    except:
        pass
    print(tex)
    try:
        import matplotlib.pyplot as plt
        tex = '$' + tex + '$'
        # Создание области отрисовки
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_axis_off()

        # Отрисовка формулы
        t = ax.text(0.5, 0.5, tex,
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=20, color='black')

        # Определение размеров формулы
        ax.figure.canvas.draw()
        bbox = t.get_window_extent()
        # print(bbox.width, bbox.height)

        # Установка размеров области отрисовки
        fig.set_size_inches(bbox.width / 80, bbox.height / 80)  # dpi=80

        # Отрисовка или сохранение формулы в файл
        plt.show()
        # plt.savefig('test.svg')
        # plt.savefig('test.png', dpi=300)
    except Exception as e:
        print(e)


def solve_latex_expression(latex):
    return eval(latex_to_python(latex))


if __name__ == '__main__':
    print(latex_to_tex(r'''
    №1. Решите уравнение $x^{\lg x}+10^{(\lg x)^2}=20$
Ответ: 0,$1 ; 10$.
№2. Решите уравнение $\log _{2 x+3}\left(x^2+4 x+4\right)+\log _{x+2}\left(2 x^2+7 x+6\right)=4$
Ответ: корней нет.
№3. Решите неравенство $(\sqrt{2}+1)^x+1<2(\sqrt{2}-1)^x$. В ответ запишите наибольшее целое число, являющееся решением неравенства.
Ответ: $(-\infty ; 0),-1$-наибольшее целое число
№4. Найдите количество целых решений неравенства
$9^{x+0,5}-28 \cdot 3^x+9 \leq 0$
Ответ: $-1 \leq x \leq 2,4$ целых решения.
№5. Решите неравенство $7 \cdot 49^{\frac{-x^2}{2}} \geq \frac{7^{|x^2+5x|}}{49}$
    '''))
