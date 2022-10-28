import re
def latex_to_python(latex):
    latex = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', latex)
    latex = re.sub(r'\^\{([^}]+)\}', r'**\1', latex)
    latex = re.sub(r'\\sqrt\{([^}]+)\}', r'\1**0.5', latex)
    latex = latex\
        .replace('\\cdot', '*')\
        .replace('\\left', '')\
        .replace('\\right', '')\
        .replace('[', '')\
        .replace(']', '')
    return latex

if __name__ == '__main__':
    expression = r'\frac{2}{3} * \sqrt{2} * \left(\frac{2}{3}\right)^{2}'
    print(latex_to_python(expression))
    print(eval(latex_to_python(expression)))