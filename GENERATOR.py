import inspect
import logging
import re
import traceback
from random import randint, choice
from latex import latex_to_tex, render_latex
from config import config
from utils import filter_dict, get_params_from_function, get_params_from_task
import sys
import __main__
from templates import latex_to_function, get_integer_roots, get_answer_of_inequality
from copy import deepcopy
def generate_inequality_test(latex, ranges, nulls=0, amount=10):
    foo = latex_to_function(latex)
    task = r'Найдите максимальное целое решение' + latex

    def solution(**k):
        roots = get_integer_roots(foo(**k), RANGE=range(-100, 100))
        if get_answer_of_inequality(foo(**k), nulls=nulls) and max(roots) != 99:
            return max(roots)
    try:
        generate_test(task, ranges, solution, amount=amount, iterations=10000)
    except:
        pass
    task = r'Найдите минимальное целое решение' + latex

    def solution(**k):
        roots = get_integer_roots(foo(**k), RANGE=range(-100, 100))
        if get_answer_of_inequality(foo(**k), nulls=nulls) and min(roots) != -100:
            return min(roots)
    try:
        generate_test(task, ranges, solution, add=True, amount=amount, iterations=10000)
    except:
        pass
    if nulls % 2 == 0:
        task = r'Найдите количество целых решений ' + latex

        def solution(**k):
            roots = get_integer_roots(foo(**k), RANGE=range(-100, 100))
            if get_answer_of_inequality(foo(**k), nulls=nulls) and roots[0] != -100 and roots[-1] != 99 and sum(roots) != 0:
                return len(roots)

        generate_test(task, ranges, solution, add=True,amount=amount//4)

        task = r'Найдите сумму целых решений ' + latex

        def solution(**k):
            roots = get_integer_roots(foo(**k), RANGE=range(-100, 100))
            if get_answer_of_inequality(foo(**k), nulls=nulls) and roots[0] != -100 and roots[-1] != 99 and sum(
                    roots) != 0 and sum(roots) < 100:
                return sum(roots)

        generate_test(task, ranges, solution, add=True,amount=amount//4 + amount % 4)

def get_py_filenames(path='./'):
    from os import walk
    filenames = next(walk(path), (None, None, []))[2]
    return [filename.split('.')[0] for filename in filenames if filename.endswith('.py')]


def get_module_names(path):
    files = get_py_filenames(path)

    def check_module(module_name):
        # try:
        #     get_test_arguments(module_name)
        # except AttributeError:
        #     return False
        return True

    files = [file for file in files if check_module(file)]
    print('Valid modules:')
    print(*[f'{i + 1}. {files[i]}' for i in range(len(files))] or ['No .py files found'], sep='\n')
    indexes_of_modules = list(map(int, input('Enter modules to generate, example (1 2 12): ').split()))
    return [files[i] for i in range(len(files)) if i + 1 in indexes_of_modules]


def write_to_file(text, filename, path='.', add=False):
    full_path = f'{path}/{config["generated_tasks_path"]}/{filename}.txt'
    print(f'Wrote to: {full_path}')
    output = open(full_path, 'a' if add else 'w', encoding='utf-8')
    output.write(text + '\n')
    output.close()


def get_test_arguments(path):
    module = __import__(path)
    return module.task, module.ranges, module.solution


def prettify_answer(answer):
    if type(answer) is float:
        if int(answer) == answer:
            return f'{int(answer)}'
        return f'{answer} ={str(answer).replace(".", ",")}'

    if (type(answer) is list or type(answer) is tuple) and int(answer[0]) == answer[0]:
        from itertools import permutations
        perm = list(permutations(set(answer)))
        return f'{"=".join([" ".join([str(int(item)) for item in answer]) + " " for answer in perm])}'

    return f'{answer}'





def prettify_task(task):
    task = task.replace('+-', '-')
    task = re.sub(r'([^123456789])1([a-zA-Z])', r'\1\2', task)
    task = re.sub(r'(-\d+)\^\\\{(\d*[02468])\\\}', r'(\1)^\{\2\}', task)
    task = re.sub(r'(-\d+)\^(\d*[02468])', r'(\1)^\{\2\}', task)
    return task


def prettify_ranges(ranges):
    for key in ranges:
        if not callable(ranges[key]):
            ranges[key] = list(ranges[key])
            ranges[key] = [i for i in ranges[key] if i != 0]
    return ranges


def get_max_nulls(task_mask, ranges):
    if not 'x' in task_mask:
        return
    if '<' in task_mask or '>' in task_mask:
        task_mask = task_mask\
            .replace('<=', '=')\
            .replace('>=', '=')\
            .replace('<', '=')\
            .replace('>', '=')
    import templates
    nulls = 0
    for i in range(1, 10):
        try:
            get_tasks(task_mask, ranges, templates.get_solution(task_mask, nulls=i), 1, 'find_nulls', iterations=20000)
            nulls = i
        except:
            break
    print('found nulls:', nulls)
    return nulls

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False
def get_variables(params, ranges):
    default_range = ranges.get('default', list(set(range(-10, 11)) - {0, 1, -1}))
    prev_variables = None
    full_list_of_params = {*params, *ranges.keys()}
    variables = {
        param: (choice(ranges[param]) if is_iterable(ranges[param]) else ranges[param])
        if param in ranges
        else choice(default_range)
        for param in full_list_of_params
    }
    while prev_variables != variables:
        prev_variables = deepcopy(variables)
        for param in full_list_of_params:
            if callable(variables[param]):
                props = filter_dict(variables, variables[param])
                try: variables[param] = variables[param](**props)
                except: pass
            if type(variables[param]) is list or type(variables[param]) is range:
                variables[param] = choice(variables[param]) if variables[param] else choice(default_range)
    return variables


def get_tasks(task_mask, ranges, solution, amount, name_of_file, iterations=1000000):
    id = str(__import__('time').time())[-5:]
    errors = 0
    ranges = prettify_ranges(ranges)
    tasks = []
    params = get_params_from_task(task_mask)
    if not params:
        from utils import replace_numbers_by_variables
        task_mask = replace_numbers_by_variables(task_mask)
        params = get_params_from_task(task_mask)
    if solution is None:
        nulls = get_max_nulls(task_mask, ranges) if 'x' in task_mask else 0
        nulls = int(input(f'Максимальное количество нулей (enter to submit {nulls=}):') or str(nulls))
        if '<' in task_mask or '>' in task_mask:
            print('generate inequality test')
            generate_inequality_test(task_mask, ranges, nulls, amount)
            return
        import templates
        solution = templates.get_solution(task_mask, nulls=nulls)
        if 'x' in task_mask:
            task_mask = 'Введите сумму корней уравнения: ' + task_mask
    params_of_solution = get_params_from_function(solution) or params
    task_mask = latex_to_tex(task_mask)
    while len(tasks) < amount:
        if not tasks:
            iterations -= 1
            if iterations == 0:
                raise Exception('iterations limit reached')
        variables = get_variables(params, ranges)
        variables = {key: variables[key] for key in params_of_solution}
        try:
            answer = solution(**variables)
        except Exception as e:
            if not errors:
                print(f'ERROR: {e} in {task_mask} with {variables}')
                traceback.print_exc()
                print('continue generate')
            errors += 1
            continue
        if not answer:
            continue
        task = task_mask
        for key in variables:
            task = task.replace(f'[{key}]', str(variables[key]))
        task = prettify_task(task)
        if len(tasks) < 3:
            render_latex(task, prettify_answer(answer))
        task = f':: id: {id} file: {name_of_file} {len(tasks)}\n:: {task}'
        task += '\n{=' + prettify_answer(answer) + '}\n'
        tasks.append(task)
        print(task)
    return tasks


def generate_test(
        task_mask: str,
        ranges: dict = {},
        solution=None,
        amount: int = config['amount_of_tasks'],
        create_file: bool = config['create_file'],
        add=False,
        **kwargs
):
    render_latex(task_mask)
    name_of_file = __main__.__file__.replace('/', '\\').split('\\')[-1].split('.')[0]
    params = task_mask.strip(), ranges, solution, amount, name_of_file
    tasks = get_tasks(*params, **kwargs)
    if create_file:
        write_to_file('\n'.join(tasks), name_of_file, '..', add=add)


if __name__ == '__main__':
    print('Enter path to modules')
    sys.path.insert(0, config['modules_path'])  # чтобы импортировать модуль из этой папки
    module_names = get_module_names(config['modules_path'])
    for module_name in module_names:
        task_mask, ranges, solution = get_test_arguments(module_name)
        render_latex(task_mask)
        params = task_mask.strip(), ranges, solution, config['amount_of_tasks'], module_name
        tasks = get_tasks(*params)
        if config['create_file']:
            write_to_file(
                '\n'.join(tasks),
                '00 Several_tests' if len(module_names) > 1 else module_names[0],
                add=True
            )
