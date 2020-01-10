import random


def generate_integer():
    return random.randint(1, 99)


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def triple_answer(counter):
    if counter < 3:
        return True
    else:
        return False


def check_answer(correct_answer, user_answer):
    if correct_answer == user_answer:
        return True
    else:
        return False
