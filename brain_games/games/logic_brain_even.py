import brain_games.game_engine
import random
import prompt


def game_even():
    user_name = brain_games.game_engine.welcome_user()
    i = 0
    print('Answer "yes" if the number is even, otherwise answer "no"')
    while i < 3:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        user_answer = prompt.string(prompt='Your answer: ', empty=False)
        true_answer = num % 2 == 0 and 'yes' or 'no'
        if user_answer != true_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{true_answer}'.")
            return print(f"Let's try again, {user_name}!")
        elif user_answer == true_answer:
            print('Correct!')
            i += 1
    return print(f"Congratulations, {user_name}!")
