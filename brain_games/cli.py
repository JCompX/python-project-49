import prompt

def welcome_user():
    a = prompt.string(prompt = 'May I have your name? ', empty = False)
    print(f'Hello, {a}!')