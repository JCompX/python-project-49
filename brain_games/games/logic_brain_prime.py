import random


def game_question():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def data_question():
    return random.randint(2, 100)


def true_answer(data_question):
    for i in range(2, data_question):
        if data_question % i == 0:
            return "no"
    return "yes"


def check_user_answer(data_question, user_answer):
    return True if true_answer(data_question) == user_answer else False
