import random


def game_question():
    return 'What number is missing in the progression?'


def data_question():
    step = random.randint(1, 4)
    ran = range(1, 20, step)
    list = []
    for i in ran:
        list.append(i)
    changed_index = random.randint(0, len(list) - 1)
    global missed_num
    missed_num = list[changed_index]
    list[changed_index] = '..'
    return " ".join(str(x) for x in list)


def true_answer(data_question):
    return missed_num


def check_user_answer(data_question, user_answer):
    return True if int(user_answer) == missed_num else False
