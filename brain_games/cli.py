import prompt


def run(game_name):
    print('Welcome to the Brain Games!')
    print_game_rules(game_name)
    user_name = prompt.string('May I have your name?\n')
    print('Hello, %s!' % user_name)
    return user_name


def print_question(number1, number2=0, sign=''):
    if number2 == 0 and sign == '':
        print("Question: %s" % (number1))
    else:
        print("Question: %s %s %s" % (number1, sign, number2))


def end(user_name):
    print("Congratulations, %s!" % user_name)


def get_answer():
    ans = prompt.string("Your answer: ")
    return ans


def print_game_rules(game_name):
    if game_name == "even":
        print('Answer "yes" if number even otherwise answer "no".\n')
    elif game_name == "calc":
        print('What is the result of the expression?')
