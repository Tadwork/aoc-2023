
import pytest

from day3 import (
    create_matrix, 
    has_symbol, 
    check_for_symbol_and_return_part,sum_of_partnumbers,
    is_part_num, 
    get_full_part_number_from_coord, 
    get_prod_of_adjacent_part_numbers_to_gear, 
    get_all_gear_coordinates
)
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

def test_is_part_num():
    matrix = [
        ['1','*','2'],
        ['3','.','4']
    ]
    assert is_part_num(matrix,0,0) == True
    assert is_part_num(matrix,0,1) == False
    assert is_part_num(matrix,-1,0) == False
    assert is_part_num(matrix,2,1) == False
    
def test_get_full_part_number_from_coord():
    matrix = [
        ['.','.','.'],
        ['1','1','1'],
        ['3','*','4']
    ]
    assert get_full_part_number_from_coord(matrix,1,1)[0] == 111
    assert get_full_part_number_from_coord(matrix,2,0)[0] == 3
    assert get_full_part_number_from_coord(matrix,2,2)[0] == 4
    
def test_get_prod_of_adjacent_part_numbers_to_gear():
    # matrix = [
    #     ['.','.','.'],
    #     ['.','.','.'],
    #     ['3','*','4']
    # ]
    # assert get_prod_of_adjacent_part_numbers_to_gear(matrix, 2, 1) == 12
    matrix = [
        ['.','.','.'],
        ['.','1','0'],
        ['3','*','.']
    ]
    assert get_prod_of_adjacent_part_numbers_to_gear(matrix, 2, 1) == 30
    matrix = [
        ['.','.','.'],
        ['.','*','.'],
        ['3','.','2']
    ]
    assert get_prod_of_adjacent_part_numbers_to_gear(matrix, 1, 1) ==6
    matrix = [
        ['.','*','1'],
        ['.','.','.'],
        ['3','.','2']
    ]
    assert get_prod_of_adjacent_part_numbers_to_gear(matrix, 0, 1) == 0
    matrix = [
        ['.','.','1'],
        ['.','*','.'],
        ['3','.','2']
    ]
    assert get_prod_of_adjacent_part_numbers_to_gear(matrix, 1, 1) == 0
    matrix = [
        ['.','.','.'],
        ['.','*','.'],
        ['2','.','2']
    ]
    assert get_prod_of_adjacent_part_numbers_to_gear(matrix, 1, 1) == 4
    
def test_get_all_gear_coordinates():
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
    assert get_all_gear_coordinates(schematic) == 467835