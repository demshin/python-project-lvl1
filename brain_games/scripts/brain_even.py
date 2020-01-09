from brain_games.cli import run, end
from brain_games.logics import triple_even


def main():
    name = run()
    triple_even()
    end(name)


if __name__ == '__main__':
    main()
