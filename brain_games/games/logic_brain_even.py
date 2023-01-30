import random
import prompt


def game_question():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def answer():
    return prompt.string(prompt='Your answer: ', empty=False)


def true_answer(data_question):
    return 'yes' if data_question % 2 == 0 else 'no'


def data_question():
    return random.randint(1, 100)


def check_user_answer(data_question, user_answer):
    if data_question % 2 == 0 and user_answer == 'yes':
        return True
    elif data_question % 2 != 0 and user_answer == 'no':
        return True
    else:
        return False
