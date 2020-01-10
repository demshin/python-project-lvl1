from brain_games.cli import run, end
from brain_games.games.even import even


def main():
    name = run('even')
    even()
    end(name)


if __name__ == '__main__':
    main()
