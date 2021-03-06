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
    elif number1 > 0 and number2 > 0 and not sign:
        print("Question: %d %d" % (number1, number2))
    else:
        print("Question: %s %s %s" % (number1, sign, number2))


def end(user_name):
    print("Congratulations, %s!" % user_name)


def get_str_answer():
    user_answer = prompt.string("Your answer: ")
    return user_answer


def get_int_answer():
    user_answer = prompt.integer("Your answer: ")
    return user_answer


def print_game_rules(game_name):
    if game_name == "even":
        print('Answer "yes" if number even otherwise answer "no".\n')
    elif game_name == "calc":
        print('What is the result of the expression?')
    elif game_name == "gcd":
        print('Find the greatest common divisor of given numbers.')


def print_correct():
    print('Correct!')


def print_incorrect(correct_ans, user_ans, user_name):
    print("'%d' is wrong answer ;(. " % user_ans, end='')
    print("Correct answer was '%d'." % correct_ans)
    print("Let's try again, %s!" % user_name)
