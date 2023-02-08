import prompt

COUNT_OF_ROUND = 3


def game_process(input_data):
    print('Welcome to the Brain Games!')
    user_name = prompt.string(prompt='May I have your name? ', empty=False)
    print(f'Hello, {user_name}!')
    print(input_data.game_question())
    i = 0
    while i < COUNT_OF_ROUND:
        data_question = input_data.data_question()
        print(f'Question: {data_question}')
        user_answer = prompt.string(prompt='Your answer: ', empty=False)
        true_answer = input_data.true_answer(data_question)
        if input_data.check_user_answer(data_question, user_answer) is True:
            print('Correct!')
        else:
            return print(f"{user_answer} is wrong answer ;(. "
                         f"Correct answer was {true_answer}.\n"
                         f"Let's try again, {user_name}!")
        i += 1
    return print(f"Congratulations, {user_name}!")
