import re


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
    python = re.sub(r'\((.*)\)\*\*0\.5', r'\\sqrt{\1}', python)
    python = re.sub(r'(.)\*\*0\.5', r'\\sqrt{\1}', python)

    python = re.sub(r'(\(.+\)|.)\*\*(\(.+\)|\\[^}]+}|.)', r'\1^{\2}', python)
    python = re.sub(r'([^*])\*([^*])', r'\1 \\cdot \2', python)
    while '/' in python:
        copy = python
        print(python)
        python = re.sub(r'(\((.+)\)|([^({})+-]*)(\{[^({})+-]*})*[^({})+-]*)'
                        r'/(\((.+)\)|([^({})+/-]*)({.*})*[^({})+/-]*)', r'\\frac{\1}{\5}', python, count=1)
        if copy == python:
            print('ERROR')
            break
    latex = python.replace('(', r'\left(').replace(')', r'\right)')
    return latex


# def python_to_latex(python):
#     stack = []
#     while python:
#         part_regex = r'(\*\*)|([\(\)\+\-\*/.0-9])'
#         part = re.search(part_regex, python).group()
#         stack.append(part)
#         python = python[len(part):]
#     print(stack)
def solve_latex_expression(latex):
    return eval(latex_to_python(latex))


if __name__ == '__main__':
    print(python_to_latex('1/(2/(1/2))**0.5**2'))
