def replace_numbers_by_variables(string):
    '''
    'x^2 + 2x + 1' -> 'x^[a]+[b]x+[c]'
    :return: string
    '''
    import re
    from string import ascii_lowercase
    for letter in ascii_lowercase:
        new = re.sub(r'([23456789]|\d{2,})', r'[{}]'.format(letter), string, 1)
        if new != string: string = new
        else: break
    return string

import inspect
def filter_dict(dict_to_filter, thing_with_kwargs):
    sig = inspect.signature(thing_with_kwargs)
    filter_keys = [param.name for param in sig.parameters.values() if param.kind == param.POSITIONAL_OR_KEYWORD]
    filtered_dict = {filter_key: dict_to_filter[filter_key] for filter_key in filter_keys}
    return filtered_dict

def get_params_from_function(func):
    return inspect.getfullargspec(func)[0]

