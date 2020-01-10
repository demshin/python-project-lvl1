from brain_games.games.logics import generate_integer, is_even, triple_answer
from brain_games.cli import print_question, get_answer


def check_answer(num):
    ans = get_answer()
    if (is_even(num) and ans == 'yes') or (not is_even(num) and ans == 'no'):
        return True
    else:
        return False


def even():
    counter = 0
    while triple_answer(counter):
        number = generate_integer()
        print_question(number)
        if check_answer(number):
            counter += 1
