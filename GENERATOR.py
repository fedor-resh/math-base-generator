import logging
import re
import traceback
from random import randint
from latex import latex_to_tex
from config import config
import sys
import __main__


def get_py_filenames(path='./'):
    from os import walk
    filenames = next(walk(path), (None, None, []))[2]
    return [filename.split('.')[0] for filename in filenames if filename.endswith('.py')]


def get_module_names(path):
    files = get_py_filenames(path)

    def check_module(module_name):
        try:
            get_test_arguments(module_name)
        except AttributeError:
            return False
        return True

    files = [file for file in files if check_module(file)]
    print('Valid modules:')
    print(*[f'{i + 1}. {files[i]}' for i in range(len(files))] or ['No .py files found'], sep='\n')
    indexes_of_modules = list(map(int, input('Enter modules to generate, example (1 2 12): ').split()))
    return [files[i] for i in range(len(files)) if i + 1 in indexes_of_modules]


def write_to_file(text, filename, path='.'):
    full_path = f'{path}/{config["generated_tasks_path"]}/{filename}.txt'
    print(f'Wrote to: {full_path}')
    output = open(full_path, 'w', encoding='utf-8')
    output.write(text)
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
        perm = list(permutations(answer))
        return f'{"=".join([" ".join([str(int(item)) for item in answer]) + " " for answer in perm])}'

    return f'{answer}'


def get_params(func):
    import inspect
    return inspect.getfullargspec(func)[0]


def prettify_task(task):
    return re.sub(r'1([a-zA-Z])', r'\1', task)


def prettify_ranges(ranges):
    for key in ranges:
        ranges[key] = list(ranges[key])
        ranges[key] = [i for i in ranges[key] if i != 0]
    return ranges


def get_tasks(task_mask, ranges, solution, amount, name_of_file):
    errors = 0
    ranges = prettify_ranges(ranges)
    tasks = []
    params = get_params(solution)
    task_mask = latex_to_tex(task_mask)
    while len(tasks) < amount:
        variables = {
            key: ranges[key][randint(0, len(ranges[key]) - 1)]
            if key in ranges else randint(2, 10)
            for key in params
        }
        try:
            answer = solution(**variables)
        except Exception as e:
            if not errors:
                print(f'ERROR: {e} in {task_mask} with {variables}')
                traceback.print_exc()
            errors += 1
            continue
        if not answer: continue

        task = f':: file: {name_of_file} {len(tasks)}\n:: {task_mask}'

        for key in variables:
            task = task.replace(f'[{key}]', str(variables[key]))
        task += '\n{=' + prettify_answer(answer) + '}\n'

        tasks.append(prettify_task(task))
        print(task)
    return tasks


def generate_test(
        task_mask: str,
        ranges: dict,
        solution: callable,
        amount: int = config['amount_of_tasks'],
        create_file: bool = config['create_file'],
):
    name_of_file = __main__.__file__.split('\\')[-1].split('.')[0]
    params = task_mask.strip(), ranges, solution, amount, name_of_file
    tasks = get_tasks(*params)
    if create_file:
        write_to_file('\n'.join(tasks), name_of_file, '..')


if __name__ == '__main__':
    sys.path.insert(0, config['modules_path'])  # чтобы импортировать модуль из этой папки
    module_names = get_module_names(config['modules_path'])
    tasks = []
    for module_name in module_names:
        task_mask, ranges, solution = get_test_arguments(module_name)
        params = task_mask.strip(), ranges, solution, config['amount_of_tasks'], module_name
        tasks += get_tasks(*params)
    if config['create_file']:
        write_to_file('\n'.join(tasks), '00 Several_tests' if len(module_names) > 1 else module_names[0])
