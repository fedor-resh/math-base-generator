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
        parts[i] = r'\\(' + parts[i] + r'\\)'

    text = ''.join(parts)
    return text


if __name__ == '__main__':
    print(latex_to_tex('$\sqrt{49}*{22}*123${=answer}$123$'))
