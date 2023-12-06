import pytest
import day6


def test_parse_input():
    input = \
"""Time: 0
Distance: 1
"""
    assert list(day6.parse_input(input)) == [(0,1)]
    
def test_parse_input_no_kerning():
    input = \
"""Time:0 1
Distance:1 2
"""
    assert list(day6.parse_input_no_kerning(input)) == [(1,12)]
    
def test_number_of_ways_to_beat_record():
    input = [(7,9),(15,40),(30,200)]
    day6.number_of_ways_to_beat_record(input) == 288
    
