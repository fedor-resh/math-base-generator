import re


def latex_to_python(latex):
    latex = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', latex)
    latex = re.sub(r'\^\{([^}]+)\}', r'**\1', latex)
    latex = re.sub(r'\\sqrt\{([^}]+)\}', r'\1**0.5', latex)
    latex = latex \
        .replace('\\cdot', '*') \
        .replace('\\left', '') \
        .replace('\\right', '') \
        .replace('[', '') \
        .replace(']', '')
    return latex

def python_to_latex(python):
    python = re.sub(r'\((.*)\)\*\*0\.5', r'\\sqrt{\1}', python)
    python = re.sub(r'(.)\*\*0\.5', r'\\sqrt{\1}', python)

    python = re.sub(r'(\(.*\)|.)\*\*(\(.*\)|.)', r'\1^{\2}', python)
    python = re.sub(r'([^*])\*([^*])', r'\1 \\cdot \2', python)
    while '/' in python:
        python = re.sub(r'([^({]*)/([^)}]*)', r'\\frac{\1}{\2}', python, count=1)

    python = python.replace('(', '').replace(')', '')
    return python

def solve_latex_expression(latex):
    return eval(latex_to_python(latex))


if __name__ == '__main__':
    print(python_to_latex('a/b/c**d'))