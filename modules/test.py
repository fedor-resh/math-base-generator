from utils import filter_dict, get_params_from_function
f = lambda a, b, c: a + b
print(filter_dict(dict(a=1, b=2, c=3, d=4), f))
print(get_params_from_function(f))