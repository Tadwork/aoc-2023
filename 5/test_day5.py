import pytest
import day5
test_input = \
"""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

class TestAlmanac:
    def test_parse_input(self):
        input = """
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        """
        almanac = day5.Almanac(input)
        assert almanac.seeds == [{'seed':79,'length':14},{'seed':55,'length':13}]
        assert almanac.seed_to_soil.get(98) == 50
        
    def test_get_location(self):
        almanac = day5.Almanac(test_input)
        assert almanac.get_location(79) == 82
        assert almanac.get_location(14) == 43
        assert almanac.get_location(55) == 86
        assert almanac.get_location(13) == 35
    
    