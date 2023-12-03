
import pytest

from day3 import create_matrix, has_symbol, check_for_symbol_and_return_part,sum_of_partnumbers

def test_create_matrix():
    schematic = """
    1.2
    3.4
    """
    assert create_matrix(schematic) == [['1','.','2'],['3','.','4']]
    
def test_has_symbol():
    matrix = [['1','*','2'],['3','.','4']]
    assert has_symbol(matrix,0,0) == False
    assert has_symbol(matrix,0,1) == True
    
def test_check_for_symbol_and_return_part():
    matrix = [
        ['1','.','2'],
        ['*','.','4']
    ]
    assert check_for_symbol_and_return_part(matrix,0,0,1) == 1
    matrix = [
        ['1','.','2'],
        ['3','*','4']
    ]
    assert check_for_symbol_and_return_part(matrix,0,0,1) == 1
    matrix = [
        ['1','*','2'],
        ['3','.','4']
    ]
    assert check_for_symbol_and_return_part(matrix,0,0,1) == 1
    matrix = [
        ['.','*','.'],
        ['1','.','2'],
        ['3','.','4']
    ]
    assert check_for_symbol_and_return_part(matrix,1,0,1) == 1
    matrix = [
        ['.','*','.'],
        ['1','.','2'],
        ['3','.','4']
    ]
    assert check_for_symbol_and_return_part(matrix,1,2,3) == 2
    matrix = [
        ['.','*','.'],
        ['1','.','2'],
        ['3','.','4']
    ]
    assert check_for_symbol_and_return_part(matrix,2,2,3) == 0
    matrix = [
        ['.','.','.'],
        ['1','.','2'],
        ['3','*','4']
    ]
    assert check_for_symbol_and_return_part(matrix,2,2,3) == 4
    
def test_sum_of_partnumbers():
    schematic = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
    sum_of_partnumbers(schematic) ==  4361