import random


def game_question():
    return 'What is the result of the expression?'


def data_question():
    int1 = random.randint(30, 70)
    int2 = random.randint(1, 30)
    chosen_operand = random.choice(['+', '-', '*'])
    return f'{int1} {chosen_operand} {int2}'


def true_answer(data_question):
    return eval(data_question)


def check_user_answer(data_question, user_answer):
    return True if int(user_answer) == true_answer(data_question) else False
