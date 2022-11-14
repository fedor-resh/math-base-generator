import re


def latex_to_python(latex):
    latex = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', latex)
    latex = re.sub(r'\^\{([^}]+)\}', r'**\1', latex)
    latex = re.sub(r'\\sqrt\{([^}]+)\}', r'(\1)**0.5', latex)
    latex = latex \
        .replace('\\cdot', '*') \
        .replace('\\left', '') \
        .replace('\\right', '') \
        .replace('[', '') \
        .replace(']', '')
    return latex


def solve_latex_expression(latex):
    return eval(latex_to_python(latex))


if __name__ == '__main__':
    print(latex_to_python(r'-\sqrt{7^{4}\cdot1^{4}}'))

    print(eval(latex_to_python(r'-\sqrt{7^{4}\cdot1^{4}}')))

