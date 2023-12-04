
import pytest

from day4 import (
    parse_card_input, 
    score_from_diff,
    process_cards_and_return_score,
    process_cards_and_return_count
)
def test_parse_card_input():
    card1 = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert parse_card_input(card1) == (1,4)
    cars2= "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"
    assert parse_card_input(cars2) == (2,2)
    
    
def test_score_from_diff():
    assert score_from_diff(1) == 1
    assert score_from_diff(2) == 2
    assert score_from_diff(3) == 4
    assert score_from_diff(4) == 8
    
def test_process_cards():
    cards = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
    assert process_cards_and_return_score(cards) ==  13
    
def test_process_cards_and_return_count():
    cards = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert process_cards_and_return_count(cards) ==  5
    cards = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
    assert process_cards_and_return_count(cards) ==  30