import prompt


def run():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = prompt.string('May I have your name?\n')
    print('Hello, ' + name + '!')
    return name


def question(number):
    print("Question: " + str(number))


def end(name):
    print("Congratulations, " + name + "!")


def get_answer():
    ans = prompt.string("Your answer: ")
    return ans
