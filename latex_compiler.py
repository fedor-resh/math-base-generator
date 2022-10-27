import re


def latex_to_tex(text):
    parts = text.split('$')
    for i in range(1, len(parts), 2):
        parts[i] = parts[i].replace('*', '\cdot')
        parts[i] = parts[i].replace('\frac', '\\\dfrac')\
            .replace('\sqrt', '\\\sqrt')\
            .replace('\left', '\\\left')\
            .replace('\right', '\\\right')\
            .replace('\cdot', '\\\cdot')\
            .replace('{', '\{')\
            .replace('}', '\}')\

    text = '$'.join(parts)
    text = re.sub(r'\$(.*)\$', r'\\\(\1\\\)', text)
    return text


if __name__ == '__main__':
    print(latex_to_tex('$\sqrt{2}sdf{asdf} * 123${}'))

