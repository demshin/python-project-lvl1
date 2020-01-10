from brain_games.cli import print_question
from brain_games.logics import generate_integer


def calc():
    print_question(generate_integer(), generate_integer(), '+')

# def get_random_operation():
