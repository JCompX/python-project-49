import random
import math


def game_question():
    return 'Find the greatest common divisor of given numbers.'


def data_question():
    num1 = random.randint(50, 100)
    num2 = random.randint(5, 50)
    return f'{num1} {num2}'


def true_answer(data_question):
    num1, num2 = data_question.split()
    num1, num2 = int(num1), int(num2)
    return math.gcd(num1, num2)


def check_user_answer(data_question, user_answer):
    return True if int(user_answer) == true_answer(data_question) else False
