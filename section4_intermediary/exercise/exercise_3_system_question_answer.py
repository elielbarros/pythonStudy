questions = [
    {
        'question': 'What is 2+2?',
        'options': ['1', '3', '4', '5'],
        'answer': '4'
    },
    {
        'question': 'What is 5*5?',
        'options': ['25', '55', '10', '51'],
        'answer': '25'
    },
    {
        'question': 'What is 10/2?',
        'options': ['4', '5', '2', '1'],
        'answer': '5'
    }
]

right_answers = 0
for question in questions:
    print(question['question'])

    for index, option in enumerate(question['options']):
        print(f'{index}) {option}')

    answer = input('Write your answer: ')
    try:
        answer_int = int(answer)

        condition = 0 <= answer_int <= len(question['options'])

        is_answer_index_between_option_index = True if condition else False

        if is_answer_index_between_option_index and question['answer'] == question['options'][answer_int]:
            print('Right Answer')
            right_answers += 1
            continue

        print('Wrong Answer')
    except ValueError:
        print('Wrong Answer')

questions_len = len(questions)
print(f'You got {right_answers} out of {questions_len} questions right.')
