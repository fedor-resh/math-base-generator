def replace_numbers_by_variables(string):
    '''
    'x^2 + 2x + 1' -> 'x^[a]+[b]x+[c]'
    :return: string
    '''
    import re
    from string import ascii_lowercase
    for letter in ascii_lowercase:
        new = re.sub(r'(\d+)', r'[{}]'.format(letter), string, 1)
        if new != string: string = new
        else: break
    return string

