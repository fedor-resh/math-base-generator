import logging
import re
import traceback
from random import randint
from latex import latex_to_tex, render_latex
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
    output.write(text+'\n')
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


def get_params(task):
    import re
    return re.findall(r'\[([a-zA-Z])\]', task)
    # import inspect
    # return inspect.getfullargspec(func)[0]


def prettify_task(task):
    task = task.replace('+-', '-')
    return re.sub(r'1([a-zA-Z])', r'\1', task)


def prettify_ranges(ranges):
    for key in ranges:
        ranges[key] = list(ranges[key])
        ranges[key] = [i for i in ranges[key] if i != 0]
    return ranges

def get_max_nulls(task_mask):
    import templates
    nulls = 0
    for i in range(1, 10):
        try:
            get_tasks(
                task_mask,
                {}, templates.get_solution(task_mask, nulls=i),
                1,'find_nulls',
                iterations=20000
            )
            nulls = i
        except:
            break
    print('found nulls:', nulls)
    return nulls


def get_tasks(task_mask, ranges, solution, amount, name_of_file, iterations=10000000):
    if solution is None:
        import templates
        nulls = get_max_nulls(task_mask)
        solution = templates.get_solution(task_mask, nulls=nulls)
    errors = 0
    ranges = prettify_ranges(ranges)
    tasks = []
    params = get_params(task_mask)
    task_mask = latex_to_tex(task_mask)
    default_range = list(set(range(-10, 10)) - {0, 1, -1})
    while len(tasks) < amount:
        if not tasks:
            iterations -= 1
            if iterations == 0:
                raise Exception('iterations limit reached')
        variables = {
            key: ranges[key][randint(0, len(ranges[key]) - 1)]
            if key in ranges else default_range[randint(0, len(default_range) - 1)]
            for key in params
        }
        try:
            answer = solution(**variables)
        except Exception as e:
            if not errors:
                print(f'ERROR: {e} in {task_mask} with {variables}')
                traceback.print_exc()
                print('continue generate')
            errors += 1
            continue
        if not answer: continue

        task = f':: file: {name_of_file} {len(tasks)}\n:: {task_mask}'

        for key in variables:
            task = task.replace(f'[{key}]', str(variables[key]))
        task += '\n{=' + prettify_answer(answer) + '}\n'
        task = prettify_task(task)
        tasks.append(task)
        print(task)
    return tasks


def generate_test(
        task_mask: str,
        ranges: dict = {},
        solution=None,
        amount: int = config['amount_of_tasks'],
        create_file: bool = config['create_file'],
        add = False,
):
    render_latex(task_mask)
    name_of_file = __main__.__file__.replace('/', '\\').split('\\')[-1].split('.')[0]
    params = task_mask.strip(), ranges, solution, amount, name_of_file
    tasks = get_tasks(*params)
    if create_file:
        write_to_file('\n'.join(tasks), name_of_file, '..', add=add)


if __name__ == '__main__':
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
