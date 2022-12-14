import re

def latex_to_tex(text):
    parts = text.split('$')
    for i in range(1, len(parts), 2):
        parts[i] = parts[i].replace('*', r'\cdot')
        parts[i] = parts[i].replace(r'\frac', r'\\dfrac') \
            .replace(r'\sqrt', r'\\sqrt') \
            .replace(r'\left', r'\\left') \
            .replace(r'\right', r'\\right') \
            .replace(r'\cdot', r'\\cdot') \
            .replace('{', r'\{') \
            .replace('}', r'\}')

        parts[i] = r'\(' + parts[i] + r'\)'
    text = ''.join(parts)

    return text

def latex_to_python(latex):
    """:return: python string"""
    if '$' in latex:
        latex = re.match(r'.*\$(.+)\$.*', latex).group(1)
    latex = re.sub(r'\^\{([^}]+)\}', r'**\1', latex)
    latex = re.sub(r'\^(\d+)', r'**\1', latex)
    latex = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1)/(\2)', latex)
    latex = re.sub(r'\\sqrt\{([^}]+)\}', r'(\1)**0.5', latex)
    latex = re.sub(r'\[([a-z])\]([a-z])', r'[\1]*\2', latex)
    latex = latex \
        .replace(r'=', '==') \
        .replace('\\cdot', '*') \
        .replace('\\left', '') \
        .replace('\\right', '') \
        .replace('\\geq', '>=') \
        .replace('\\leq', '<=') \
        .replace('$', '')\
        .replace('[','') \
        .replace(']', '')
    latex = re.sub(r'\\([a-z]+)\{([^}]+)\}', r'math.\1(\2)', latex)
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
        # ???????????????? ?????????????? ??????????????????
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_axis_off()

        # ?????????????????? ??????????????
        t = ax.text(0.5, 0.5, tex,
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=20, color='black')

        # ?????????????????????? ???????????????? ??????????????
        ax.figure.canvas.draw()
        bbox = t.get_window_extent()
        # print(bbox.width, bbox.height)

        # ?????????????????? ???????????????? ?????????????? ??????????????????
        fig.set_size_inches(bbox.width / 80, bbox.height / 80)  # dpi=80

        # ?????????????????? ?????? ???????????????????? ?????????????? ?? ????????
        plt.show()
        # plt.savefig('test.svg')
        # plt.savefig('test.png', dpi=300)
    except Exception as e:
        print(e)


def solve_latex_expression(latex):
    return eval(latex_to_python(latex))


if __name__ == '__main__':
    print(latex_to_python(r'\(2*\sqrt{2}\)'))

