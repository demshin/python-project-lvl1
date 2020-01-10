import random
from brain_games.cli import print_question, get_str_answer


def generate_integer():
    return random.randint(1, 99)


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def answer(num):
    ans = get_str_answer()
    if (is_even(num) and ans == 'yes') or (not is_even(num) and ans == 'no'):
        return True
    else:
        return False


def triple_even():
    counter = 0
    while counter < 3:
        number = generate_integer()
        print_question(number)
        if answer(number):
            counter += 1
