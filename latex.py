import re

def latex_to_tex(text):
    parts = text.split('$')
    for i in range(1, len(parts), 2):
        parts[i] = parts[i].replace('*', r'\cdot')
        render_latex(parts[i])
        parts[i] = parts[i].replace(r'\frac', r'\\dfrac') \
            .replace(r'\sqrt', r'\\sqrt') \
            .replace(r'\left', r'\\left') \
            .replace(r'\right', r'\\right') \
            .replace(r'\cdot', r'\\cdot') \
            .replace('{', r'\{') \
            .replace('}', r'\}')

        parts[i] = r'\\(' + parts[i] + r'\\)'
    text = ''.join(parts)

    return text

def latex_to_python(latex):
    """:return: python string"""
    latex = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', latex)
    latex = re.sub(r'\^\{([^}]+)\}', r'**\1', latex)
    latex = re.sub(r'\\sqrt\{([^}]+)\}', r'\1**0.5', latex)
    latex = latex \
        .replace('\\cdot', '*') \
        .replace('\\left', '') \
        .replace('\\right', '') \
        .replace('[', '') \
        .replace(']', '')
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
    try:
        import matplotlib.pyplot as plt
        tex = f'${tex}$'
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
    pass
