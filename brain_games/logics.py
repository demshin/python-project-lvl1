import random
from brain_games.cli import question, get_answer


def generate_integer():
    return random.randint(1, 9999)


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def answer(num):
    ans = get_answer()
    if (is_even(num) and ans == 'yes') or (not is_even(num) and ans == 'no'):
        return True
    else:
        return False


def triple_even():
    counter = 0
    while counter < 3:
        number = generate_integer()
        question(number)
        if answer(number):
            counter += 1
