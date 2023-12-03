import pytest

from day2 import sum_and_power_of_possible_games, is_possible_game, get_cubes_for_turn, Game

def test_get_cubes():
    turn = '4 blue, 14 green, 7 red'
    assert get_cubes_for_turn(turn) == Game(blue=4, green=14, red=7)


def test_is_possible_game():
    assert is_possible_game(['4 blue, 14 green, 7 red'], Game(blue=4, green=14, red=7)) == (True, Game(blue=4, green=14, red=7))
    assert is_possible_game(['4 blue, 14 green, 7 red','1 blue, 1 green, 1 red'], Game(blue=10, green=10, red=10)) == (False, Game(blue=4, green=14, red=7))

def test_sum_ids_of_possible_games():
    games = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
    total,power = sum_and_power_of_possible_games(games,Game(red=12,green=13,blue=14 ))
    assert total ==  8
    assert power ==  2286