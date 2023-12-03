import pytest


from main import read_calibration_document_and_return_sum

def test_replaces_spelled_with_number():
    assert read_calibration_document_and_return_sum('1zero') == 10

def test_replaces_spelled_out_number__from_():
    assert read_calibration_document_and_return_sum('1zero') == 10
def test_add_a_single_number_to_itself():
    assert read_calibration_document_and_return_sum('1') == 11
def test_adds_the_beg_and_end_numbers():
    assert read_calibration_document_and_return_sum('12') == 12
def test_skips_non_numeric():
    assert read_calibration_document_and_return_sum('aaa1aa2a3aaa') ==  13
def test_skips_empty_lines_and_sums():
    assert read_calibration_document_and_return_sum("""
    1
    12
    aaa1aa2a3aaa
    """) ==  36
    
def test_sums_spelled_out_numbers_correctly():
    calibration_document = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
    assert read_calibration_document_and_return_sum(calibration_document) ==  281
