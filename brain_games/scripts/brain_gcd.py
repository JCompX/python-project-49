#!/usr/bin/env python3

from brain_games.games import logic_brain_gcd
from brain_games.game_engine import game_process


def main():
    game_process(logic_brain_gcd)


if __name__ == '__main__':
    main()
