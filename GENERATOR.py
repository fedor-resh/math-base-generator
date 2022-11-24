from random import randint
from latex_to_tex import latex_to_tex
from config import config
import sys
import __main__


def get_py_filenames(path='./'):
    from os import walk
    filenames = next(walk(path), (None, None, []))[2]
    return [filename.split('.')[0] for filename in filenames if filename.endswith('.py')]


def write_to_file(text, filename, path='.'):
    print(f'{path}/{config["generated_tasks_path"]}/{filename}.txt')
    output = open(f'{path}/{config["generated_tasks_path"]}/{filename}.txt', 'w', encoding='utf-8')
    output.write(text)
    output.close()


def get_test_arguments(path):
    module = __import__(path)
    return module.task, module.ranges, module.solution

def handle_answer(answer):
    if type(answer) is float:
        if int(answer) == answer:
            return f'={int(answer)}'
        return f'={answer} ={str(answer).replace(".", ",")}'
    return f'={answer}'

def get_tasks(task_mask, ranges, solution, amount, name_of_file):
    tasks = []
    while len(tasks) < amount:
        variables = {
            key: ranges[key][randint(0, len(ranges[key]) - 1)]
            for key in ranges
        }

        answer = solution(**variables)
        if not answer: continue

        task = f'::file: {name_of_file} {len(tasks)}\n:: {task_mask}'

        for key in variables:
            task = task.replace(f'[{key}]', str(variables[key]))
        task += '{' + handle_answer(answer) + '}'

        task = latex_to_tex(task)
        tasks.append(task.strip() + '\n')
    return tasks


def get_module_name(path):
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
    return files[int(input('Enter number of file: ')) - 1]


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
    print(*tasks, sep='\n')
    if create_file:
        write_to_file('\n'.join(tasks), name_of_file, '..')
        print('Wrote to file:', f'{name_of_file}.txt')


if __name__ == '__main__':
    sys.path.insert(0, config['modules_path'])  # чтобы импортировать модуль из этой папки
    module_name = get_module_name(config['modules_path'])

    task_mask, ranges, solution = get_test_arguments(module_name)

    params = task_mask.strip(), ranges, solution, config['amount_of_tasks'], module_name
    tasks = get_tasks(*params)
    print(*tasks, sep='\n')
    if config['create_file']:
        write_to_file('\n'.join(tasks), module_name)
        print('Wrote to file:', f'{module_name}.txt')
