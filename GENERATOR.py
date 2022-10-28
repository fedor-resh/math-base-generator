from random import randint
from latex_compiler import latex_to_tex
from config import config
import sys


def get_py_filenames(path='./'):
    from os import walk
    filenames = next(walk(path), (None, None, []))[2]
    return [filename.split('.')[0] for filename in filenames if filename.endswith('.py')]


def write_to_file(text, filename):
    output = open(f'{config["generated_tasks_path"]}/{filename}.txt', 'w')
    output.write(text)
    output.close()


def get_test_arguments(path):
    module = __import__(path)
    return module.task, module.ranges, module.solution


def generate_wrong_answers(ranges, solution):
    wrong_answers = []
    while len(wrong_answers) < 4:
        variables = {
            key: ranges[key][randint(0, len(ranges[key]) - 1)]
            for key in ranges
        }
        answer = solution(**variables)
        if answer: wrong_answers.append(answer)
    return wrong_answers


def get_tasks(task_mask, ranges, solution, amount):
    tasks = []
    while len(tasks) < amount:
        variables = {
            key: ranges[key][randint(0, len(ranges[key]) - 1)]
            for key in ranges
        }

        answer = solution(**variables)
        if not answer: continue

        task = task_mask
        for key in variables:
            task = task.replace(f'[{key}]', str(variables[key]))
        task = task + '{=' + str(answer) + '}'
        if '$' in task:
            task = latex_to_tex(task)
        tasks.append(task.strip() + '\n')
    return tasks


def get_tasks_with_choose(task_mask, ranges, solution, amount):
    tasks = []
    answers = generate_wrong_answers(ranges, solution)
    while len(tasks) < amount:
        index_of_correct_answer = randint(0, 3)
        variables = {
            key: ranges[key][randint(0, len(ranges[key]) - 1)]
            for key in ranges
        }
        answer = solution(**variables)
        if not answer: continue

        task = task_mask
        task += '{'
        answers[index_of_correct_answer] = answer
        for i in range(4):
            if i == index_of_correct_answer:
                task += f'\n={answers[i]}'
            else:
                task += f'\n~{answers[i]}'
        task += '\n}'
        for key in variables:
            task = task.replace(f'[{key}]', str(variables[key]))
        if '$' in task:
            task = latex_to_tex(task)
        tasks.append(task.strip() + '\n')
    return tasks


def get_module_name(path):
    files = get_py_filenames(path)

    print(*[f'{i + 1}. {files[i]}' for i in range(len(files))] or ['No .py files found'], sep='\n')
    return files[int(input('Enter number of file: ')) - 1]


module_name = get_module_name(config['modules_path'])
sys.path.insert(0, config['modules_path'])  # чтобы импортировать модуль из этой папки

task_mask, ranges, solution = get_test_arguments(module_name)

params = task_mask, ranges, solution, config['amount_of_tasks']
tasks = get_tasks_with_choose(*params) if config['type_of_test'] == 'choice' else get_tasks(*params)
print(*tasks, sep='\n')
if config['create_file']:
    write_to_file('\n'.join(tasks), module_name)
    print('Wrote to file:', f'{module_name}.txt')
