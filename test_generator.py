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
        task = task + '{=' + answer + '}'
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


def get_path():
    files = get_py_filenames()

    print(*[f'{i + 1}. {files[i]}' for i in range(len(files))] or ['No .py files found'], sep='\n')
    return files[int(input('Enter number of file: ')) - 1]


path = get_path()

task_mask, ranges, solution = get_test_arguments(path)

amount_of_tasks = int(input('Amount of tests: '))
test_type_is_choose = 'y' == input('type of test "choice"? (y/n): ').lower()
if test_type_is_choose:
    tasks = get_tasks_with_choose(task_mask, ranges, solution, amount_of_tasks)
else:
    tasks = get_tasks(task_mask, ranges, solution, amount_of_tasks)
print(*tasks, sep='\n')
if name := input('Create file (press enter to pass), name: '):
    write_to_file('\n'.join(tasks), name)
    print('\nWrote to file:', f'{name}_test.txt')
