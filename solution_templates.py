def solve_inequality(a):
    answer = ''
    prev = None
    for x in range(-1000, 1000):
        analize = [x - 0.0000001 >= a, x >= a, x + 0.0000001 >= a]
        if prev and x == 999:
            answer += '+inf)'
        if prev and x == -999:
            answer += '(-inf,'
        if all(analize) or not any(analize):
            continue
        prev = analize[2]
        if analize[1] == analize[2] == True:
            answer += f'[{x};'
        elif analize[0] == analize[1] == True:
            answer += f'{x}]'
        elif analize[2]:
            answer += f'({x};'
        elif analize[0]:
            answer += f'{x})'
        elif analize[1]:
            answer += f'{{{x}}}'
        else:
            print('Error')
    return answer