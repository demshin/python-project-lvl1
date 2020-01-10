import prompt


def run():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = prompt.string('May I have your name?\n')
    print('Hello, ' + name + '!')
    return name


def print_question(number1, number2=0, sign=''):
    if number2 == 0 and sign == '':
        print("Question: %s" % (number1))
    else:
        print("Question: %s %s %s" % (number1, sign, number2))


def end(name):
    print("Congratulations, " + name + "!")


def get_answer():
    ans = prompt.string("Your answer: ")
    return ans
