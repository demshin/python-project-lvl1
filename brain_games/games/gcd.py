from brain_games.games.logics import triple_answer, check_answer
from brain_games.games.logics import generate_integer
from brain_games.cli import print_question, print_correct
from brain_games.cli import get_int_answer


def gcd():
    counter = 0
    while triple_answer(counter):
        number1 = generate_integer()
        number2 = generate_integer()
        print_question(number1, number2)
        correct_answer = calculate_gcd(number1, number2)
        user_answer = get_int_answer()
        if check_answer(correct_answer, user_answer):
            counter += 1
            print_correct()


def calculate_gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    gcd = number1 + number2
    return gcd
