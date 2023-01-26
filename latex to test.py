def write_to_file(text, add=False):
    full_path = f'test.txt'
    output = open(full_path, 'a' if add else 'w', encoding='utf-8')
    output.write(text + '\n')
    output.close()
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
        parts[i] = parts[i].replace(' ', '')

        parts[i] = r'\(' + parts[i] + r'\)'
    text = ''.join(parts)
    return text

while x:=input('Enter latex: '):
    s = x
    while x:=input():
        s += x
    task = f'::test\n:: {s}'
    anw = input('anw: ')
    task += '\n{=' + anw + '}\n'
    write_to_file(latex_to_tex(task), add=True)
print('done')

