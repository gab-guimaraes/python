perguntas = {
    'Question 1': {
        'question': '2+2 is?',
        'answers': dict(a='1', b='4', c='6'),
        'correct_answer': 'b',
    },
    'Question 2': {
        'question': '5+5 is?',
        'answers': dict(a='10', b='0', c='2'),
        'correct_answer': 'a',
    }
}

for pk, pv in perguntas.items():
    print(f'{pk}:{pv["question"]}')

    for rk, rv in pv['answers'].items():
        print(f'[{rk}]: {rv}')



print(perguntas)
