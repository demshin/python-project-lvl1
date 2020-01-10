import random
from brain_games.cli import print_question, print_correct, print_incorrect
from brain_games.cli import get_int_answer
from brain_games.games.logics import generate_integer
from brain_games.games.logics import triple_answer, check_answer


def calc(user_name):
    counter = 0
    while triple_answer(counter):
        number1 = generate_integer()
        number2 = generate_integer()
        operation_sign = get_random_operation()
        print_question(number1, number2, operation_sign)
        correct_answer = calculate(number1, number2, operation_sign)
        user_answer = get_int_answer()
        if check_answer(correct_answer, user_answer):
            counter += 1
            print_correct()
        else:
            print_incorrect(correct_answer, user_answer, user_name)


def get_random_operation():
    operators = ('+', '-', '*')
    return random.choice(operators)


def calculate(number1, number2, operation_sign):
    if operation_sign == '+':
        return number1 + number2
    elif operation_sign == '-':
        return number1 - number2
    elif operation_sign == '*':
        return number1 * number2
