from brain_games.cli import run, end
from brain_games.games.gcd import gcd


def main():
    name = run('gcd')
    gcd()
    end(name)


if __name__ == '__main__':
    main()
