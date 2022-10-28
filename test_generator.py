from random import randint
from latex_compiler import latex_to_tex
def get_py_filenames(path='./'):
    from os import walk
    filenames = next(walk(path), (None, None, []))[2]
    return [filename.split('.')[0] for filename in filenames if filename.endswith('.py')]


def write_to_file(text, filename):
    output = open(f'{filename}_test.txt', 'w')
    output.write(text)
    output.close()


def get_test_arguments(path):
    module = __import__(path)
    return module.task, module.ranges, module.solution

def generate_wrong_answers(ranges, solution):
    wrong_answers = []
    for i in range(3):
        variables = {
            key: ranges[key][randint(0, len(ranges[key]) - 1)]
            for key in ranges
        }
        wrong_answers.append(solution(**variables))
    return wrong_answers

def get_tasks(task_mask, ranges, solution, amount):
    tasks = []
    while len(tasks) < amount:
        variables = {
            key: ranges[key][randint(0, len(ranges[key]) - 1)]
            for key in ranges
        }
        variables['answer'] = solution(**variables)
        if not variables['answer']: continue

        task = task_mask
        for key in variables:
            task = task.replace(f'[{key}]', str(variables[key]))
        if '$' in task:
            task = latex_to_tex(task)
        tasks.append(task.strip())
    return tasks


def get_path():
    files = get_py_filenames()

    print(*[f'{i + 1}. {files[i]}' for i in range(len(files))] or ['No .py files found'], sep='\n')
    return files[int(input('Enter number of file: ')) - 1]


path = get_path()

task_mask, ranges, solution = get_test_arguments(path)
amount_of_tasks = int(input('Количество заданий: '))

tasks = get_tasks(task_mask, ranges, solution, amount_of_tasks)
print(*tasks, sep='\n')
if name := input('Create file (press enter to pass), name: '):
    write_to_file('\n'.join(tasks), name)
    print('\nWrote to file:', f'{name}_test.txt')
