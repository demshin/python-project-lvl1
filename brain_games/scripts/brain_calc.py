from brain_games.cli import run, end
from brain_games.games.calc import calc


def main():
    name = run('calc')
    calc()
    end(name)


if __name__ == '__main__':
    main()
