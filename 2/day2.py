## Part 1
# You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

# The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

# As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

# You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

# For example, the record of a few games might look like this:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

## part 2

# The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

# As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

# Again consider the example games from earlier:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
# Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
# Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
# Game 4 required at least 14 red, 3 green, and 15 blue cubes.
# Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?



def get_cubes_for_turn(turn:str) -> dict:
    cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for cube in turn.split(','):
        count, color = cube.strip().split(' ')
        cubes[color] = int(count)
    return cubes

def is_possible_game(turns:list, max_colors:dict) -> bool:
    cubes_used = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    is_valid = True
    for turn in turns:
        cubes = get_cubes_for_turn(turn)
        if cubes['red'] > max_colors['red'] or cubes['green'] > max_colors['green'] or cubes['blue'] > max_colors['blue']:
            is_valid = False
        cubes_used['red'] = max(cubes['red'], cubes_used['red'])
        cubes_used['blue'] = max(cubes['blue'], cubes_used['blue'])
        cubes_used['green'] = max(cubes['green'], cubes_used['green'])
    return is_valid, cubes_used

def sum_and_power_of_possible_games(games:str, max_colors:dict) -> int:
    total_power = 0
    total = 0
    for game in games.split('\n'):
        if not game:
            continue
        game_id, turns = game.split(':')
        game_id = int(game_id[5:])
        is_valid, cubes_used = is_possible_game(turns.split(';'), max_colors)
        if is_valid:
            total += game_id
        total_power+=cubes_used['red'] * cubes_used['blue'] * cubes_used['green']
    return total, total_power

games = """
Game 1: 10 red, 7 green, 3 blue; 5 blue, 3 red, 10 green; 4 blue, 14 green, 7 red; 1 red, 11 green; 6 blue, 17 green, 15 red; 18 green, 7 red, 5 blue
Game 2: 13 green, 10 red; 11 green, 1 blue, 7 red; 5 red, 12 green, 1 blue; 12 green, 6 red; 8 green, 5 red; 12 green, 1 red
Game 3: 7 green, 1 blue; 1 blue, 3 green, 1 red; 1 green, 1 blue; 2 green; 1 blue, 7 green, 2 red; 2 green
Game 4: 7 green, 11 blue; 12 blue, 7 green; 1 green, 7 blue; 5 blue, 2 green; 5 red, 9 green, 14 blue
Game 5: 2 red, 6 blue, 6 green; 2 red, 6 green; 12 blue, 5 red, 3 green; 12 green, 5 red, 8 blue; 10 blue, 5 green; 2 red, 4 green
Game 6: 8 blue, 1 red, 17 green; 7 blue; 10 green, 6 blue; 5 blue, 1 red, 11 green
Game 7: 1 blue, 2 red, 2 green; 1 blue, 3 green; 3 green, 1 red, 3 blue; 2 blue, 3 green, 1 red
Game 8: 3 green, 10 red, 15 blue; 1 green, 9 red; 9 blue, 2 green, 12 red
Game 9: 4 green, 10 blue, 13 red; 16 red, 7 blue; 14 red, 1 green, 1 blue; 14 red, 4 blue, 1 green
Game 10: 6 blue, 9 red, 3 green; 9 green, 7 blue, 9 red; 2 red, 4 blue, 6 green; 12 green, 7 blue, 5 red
Game 11: 1 green, 6 blue, 6 red; 7 red, 1 blue; 1 green, 6 blue; 4 red, 1 green, 1 blue; 6 red, 9 green, 4 blue; 5 green, 7 red, 4 blue
Game 12: 18 green, 4 red, 12 blue; 7 green, 5 blue, 3 red; 7 green, 3 red; 8 green, 7 blue; 4 red, 7 green, 10 blue
Game 13: 1 red, 2 blue; 1 red, 6 green; 5 blue, 2 red, 12 green; 1 red, 11 green, 2 blue; 2 red, 8 green, 1 blue; 3 blue, 16 green, 1 red
Game 14: 3 blue, 2 green; 4 green, 1 red; 1 green, 1 red, 3 blue; 4 blue, 3 green; 5 blue, 1 green; 4 green, 2 blue, 1 red
Game 15: 12 blue, 3 red; 5 blue, 2 red, 1 green; 12 blue, 3 red, 2 green; 1 green, 5 red, 6 blue; 1 green, 5 blue, 3 red
Game 16: 8 red, 4 blue, 1 green; 15 blue, 5 red, 4 green; 3 green, 13 blue, 4 red; 4 red, 1 blue, 3 green; 1 green, 13 blue, 6 red
Game 17: 8 red, 7 green, 2 blue; 6 green, 1 blue, 12 red; 3 red; 4 green, 1 red; 7 red, 1 blue, 9 green
Game 18: 7 blue, 10 red, 3 green; 3 green, 1 blue; 7 red, 1 green, 7 blue; 7 blue, 4 red, 1 green; 2 green, 1 blue, 10 red; 3 blue, 11 red, 1 green
Game 19: 10 red, 10 blue; 13 red; 4 blue, 15 red, 3 green; 6 green, 11 red, 11 blue; 4 blue, 8 red
Game 20: 1 blue, 9 green, 2 red; 2 blue, 4 red, 4 green; 4 green, 2 red
Game 21: 13 green, 1 red; 3 red, 5 green, 11 blue; 1 blue, 2 red, 4 green; 7 blue, 3 red; 2 red, 1 blue, 3 green
Game 22: 2 red, 2 blue, 3 green; 10 red, 4 blue; 8 blue, 8 green, 11 red
Game 23: 1 red, 2 blue; 1 blue, 1 green; 1 green; 3 red, 1 blue, 1 green
Game 24: 12 green, 4 red, 2 blue; 8 green, 5 blue; 8 green, 2 blue, 2 red
Game 25: 3 red, 8 green; 1 red, 4 blue, 1 green; 6 green; 3 blue, 5 green, 3 red; 9 green, 3 blue, 5 red
Game 26: 1 green, 3 red, 2 blue; 7 red, 2 green, 11 blue; 7 blue, 4 red; 11 blue, 1 red, 1 green; 2 green, 10 blue, 1 red; 1 green, 7 red, 7 blue
Game 27: 5 green, 2 red, 4 blue; 5 red, 4 blue, 3 green; 5 green, 2 red, 7 blue; 7 red, 15 green, 5 blue
Game 28: 1 green, 7 blue, 14 red; 7 green, 6 blue, 3 red; 7 blue, 4 red, 10 green; 9 red, 11 green, 5 blue
Game 29: 4 red, 6 blue, 5 green; 12 red, 3 green, 1 blue; 6 blue, 11 red, 6 green; 2 green, 2 blue, 12 red
Game 30: 13 green, 11 red, 11 blue; 7 green, 9 blue, 7 red; 11 red, 1 blue, 11 green
Game 31: 14 green, 1 blue, 8 red; 1 green, 2 blue; 1 green, 1 red, 1 blue
Game 32: 7 blue, 2 green; 12 blue, 7 green; 4 red, 14 blue, 2 green; 14 green, 4 blue
Game 33: 5 blue, 12 red; 3 blue, 4 red, 1 green; 9 red, 2 blue; 11 red
Game 34: 1 blue; 3 blue; 1 blue, 1 red; 5 red, 2 blue; 4 red, 1 blue, 1 green
Game 35: 3 green, 2 blue, 1 red; 2 red, 8 green, 3 blue; 7 green, 2 red, 8 blue; 3 blue, 4 green
Game 36: 10 green, 9 blue, 2 red; 3 green, 7 blue, 7 red; 14 green, 13 blue; 8 green, 8 red, 2 blue
Game 37: 3 red, 1 blue, 14 green; 1 blue, 1 green; 5 red, 9 green; 1 red, 2 blue, 13 green; 11 red, 14 green, 2 blue
Game 38: 4 green, 3 red, 6 blue; 18 red, 15 blue, 1 green; 17 blue, 6 green, 19 red; 18 red, 15 blue; 1 green, 12 blue, 18 red
Game 39: 1 red; 10 blue, 6 red, 1 green; 1 green, 1 red, 9 blue; 17 red, 10 blue
Game 40: 5 red, 3 green, 9 blue; 8 red, 4 blue; 2 green, 3 blue, 4 red; 3 blue, 4 red, 6 green; 4 blue, 5 red, 2 green; 4 blue
Game 41: 6 green, 1 blue; 5 blue, 3 green, 6 red; 10 red, 1 blue; 6 green, 1 blue, 9 red
Game 42: 1 red, 5 green, 7 blue; 7 red, 4 blue, 4 green; 5 red, 2 green, 6 blue
Game 43: 1 green, 18 red, 8 blue; 7 red, 4 green, 5 blue; 1 blue, 18 red; 5 red, 8 blue
Game 44: 3 blue, 10 green; 5 green, 2 red, 1 blue; 6 blue, 14 green; 3 green, 5 blue, 5 red
Game 45: 12 red, 1 blue, 16 green; 1 red, 6 blue, 3 green; 5 red, 5 blue, 7 green; 8 red, 15 green; 3 green, 12 red, 7 blue
Game 46: 3 red, 1 green; 1 green, 17 blue, 10 red; 2 green, 17 blue; 3 green, 17 blue, 12 red; 2 green, 12 red
Game 47: 3 green, 9 red; 3 red, 1 blue, 6 green; 10 red, 9 green, 1 blue; 2 blue, 15 green; 7 red, 12 green, 3 blue
Game 48: 4 green, 13 red, 14 blue; 8 red, 8 green; 15 blue, 4 red, 11 green; 3 blue, 3 red, 4 green; 2 blue, 6 red, 4 green; 13 green, 12 blue, 11 red
Game 49: 15 blue, 2 green, 7 red; 1 green, 7 red, 7 blue; 13 blue; 3 blue, 2 red, 1 green
Game 50: 9 red; 5 green, 2 blue, 10 red; 5 red, 1 green
Game 51: 3 green, 1 blue, 3 red; 4 blue, 4 red; 4 green, 6 red, 5 blue; 4 red, 7 blue
Game 52: 10 green, 12 red, 2 blue; 2 green, 7 red; 18 green, 3 red, 3 blue; 6 red, 13 green, 2 blue
Game 53: 13 blue, 2 green; 2 green, 12 blue; 1 green, 11 blue, 1 red; 11 blue, 2 green, 8 red
Game 54: 5 red; 15 green, 17 red, 7 blue; 14 green, 5 red, 15 blue; 2 red, 10 blue, 16 green
Game 55: 1 blue, 1 red, 2 green; 5 green, 3 blue, 8 red; 6 red, 4 blue, 7 green; 2 blue, 10 green, 7 red
Game 56: 1 blue, 8 red, 7 green; 3 green, 7 blue, 5 red; 5 green, 7 blue; 3 blue, 12 red, 8 green; 3 blue; 2 blue, 3 green, 10 red
Game 57: 5 red, 13 green, 3 blue; 19 green, 7 red, 8 blue; 1 red, 12 green, 3 blue; 4 green, 10 blue, 4 red; 3 blue, 7 red, 20 green
Game 58: 8 blue, 5 red, 2 green; 4 red, 11 blue; 9 blue, 6 green, 8 red; 7 green, 11 blue
Game 59: 7 red, 7 green, 9 blue; 5 red, 4 green, 5 blue; 1 red, 2 blue, 6 green; 10 green, 12 blue, 3 red; 7 green, 18 blue, 4 red
Game 60: 12 blue, 7 red, 12 green; 18 green, 9 red; 13 green, 13 red, 12 blue; 14 red, 5 green, 13 blue; 17 green, 7 red, 13 blue
Game 61: 5 blue; 2 blue, 10 green, 2 red; 12 green, 2 red, 1 blue; 4 blue, 2 green; 2 red, 6 green; 6 green, 2 blue, 2 red
Game 62: 2 blue, 5 red, 4 green; 3 green, 6 blue, 7 red; 13 red, 5 blue, 1 green; 3 red, 3 blue, 1 green; 17 blue, 4 green, 3 red; 5 red, 13 blue, 3 green
Game 63: 1 red, 6 blue, 10 green; 1 red, 8 blue, 6 green; 7 red, 11 blue
Game 64: 11 blue, 13 red; 12 blue, 6 red; 1 green, 2 blue, 4 red
Game 65: 1 green, 9 red, 4 blue; 11 blue, 3 green; 2 blue, 1 green; 3 red, 2 green, 10 blue
Game 66: 8 red, 1 blue, 3 green; 1 green, 3 blue, 1 red; 2 blue, 9 green; 8 green, 3 blue, 6 red; 2 blue, 12 green, 7 red
Game 67: 5 green, 5 red, 10 blue; 12 blue, 13 green, 4 red; 6 red, 11 green, 3 blue; 8 blue, 4 red; 4 red, 14 green; 1 red, 1 blue, 14 green
Game 68: 7 green, 17 red; 14 green, 1 blue, 1 red; 11 green, 1 blue, 16 red
Game 69: 11 red, 2 green, 2 blue; 4 blue, 14 red; 2 red, 6 blue, 3 green; 6 red, 2 green; 5 red, 1 green, 4 blue; 7 red, 3 blue
Game 70: 18 blue, 4 red; 5 red, 14 blue; 17 blue, 9 red; 13 red, 17 blue, 1 green; 2 blue, 9 red
Game 71: 1 green, 6 red, 6 blue; 6 green, 4 blue, 5 red; 8 red, 3 blue, 7 green; 7 red, 2 blue, 1 green; 3 blue, 2 green, 3 red
Game 72: 11 green, 4 red, 2 blue; 2 blue, 6 green, 1 red; 3 red, 1 blue, 9 green; 4 blue, 12 green, 3 red; 2 red, 3 green, 1 blue
Game 73: 1 blue, 12 red; 14 green, 2 blue, 10 red; 6 blue, 8 red, 8 green; 7 green; 6 red, 10 green, 4 blue; 4 green, 9 red
Game 74: 5 green, 6 blue; 1 green, 12 blue; 2 blue, 2 green, 5 red; 5 green, 9 blue, 2 red
Game 75: 11 red, 7 blue, 12 green; 7 blue, 8 red, 9 green; 3 red, 17 green, 3 blue
Game 76: 1 green, 12 blue; 11 blue, 7 green, 10 red; 10 green, 12 blue, 1 red; 10 green, 12 red, 1 blue
Game 77: 2 blue, 17 green, 3 red; 10 red, 13 green; 12 green, 2 blue, 13 red; 12 green, 2 blue, 8 red; 14 green, 10 red, 1 blue
Game 78: 3 red, 8 green, 5 blue; 8 green, 3 blue; 2 green, 6 red; 4 red, 1 green, 4 blue; 4 red, 8 green, 6 blue; 1 red, 1 blue, 8 green
Game 79: 1 green, 2 blue, 2 red; 1 blue, 19 red, 1 green; 18 red; 1 green, 3 red, 5 blue; 15 red, 1 blue; 2 blue, 17 red, 1 green
Game 80: 13 red, 1 green; 15 red, 1 blue; 8 red, 1 green
Game 81: 1 blue, 1 red, 2 green; 1 red, 3 green, 2 blue; 1 blue, 4 green; 2 green, 2 blue
Game 82: 8 red, 4 green, 8 blue; 4 green, 6 red, 3 blue; 3 red, 3 blue; 2 blue, 1 green, 11 red; 2 green, 1 blue, 4 red
Game 83: 1 red, 15 green; 2 red, 6 blue, 12 green; 3 green, 10 blue, 14 red; 6 blue, 7 red, 1 green
Game 84: 2 blue, 12 red, 4 green; 1 red, 3 blue, 5 green; 6 blue, 5 green, 12 red; 2 red, 1 green; 2 red, 5 blue, 5 green
Game 85: 4 red; 3 red, 15 green, 2 blue; 15 green, 1 red, 2 blue; 4 green, 4 red, 2 blue
Game 86: 1 green, 3 red, 4 blue; 2 green, 7 red, 4 blue; 7 red, 4 green, 4 blue; 1 blue, 11 red, 4 green
Game 87: 5 green, 5 red, 15 blue; 4 blue, 12 red, 10 green; 3 green, 11 blue, 9 red; 3 red, 4 green, 16 blue; 3 red, 10 blue, 10 green; 15 blue, 9 green, 12 red
Game 88: 2 green, 10 blue; 4 blue, 8 green; 8 green, 1 blue; 13 blue, 1 red, 2 green; 2 green, 16 blue
Game 89: 5 blue, 7 red; 10 red, 11 blue, 6 green; 6 green, 3 red, 7 blue; 5 green, 3 red, 20 blue; 8 red, 6 green, 10 blue; 7 blue, 5 green, 10 red
Game 90: 4 red, 1 green, 4 blue; 9 red, 9 blue, 9 green; 4 green, 11 red; 9 red, 5 green, 3 blue; 9 red, 2 green, 2 blue
Game 91: 13 green, 13 blue; 3 red, 11 green, 5 blue; 10 blue, 3 green, 1 red; 3 blue, 10 green, 2 red; 5 blue, 2 green
Game 92: 8 blue, 1 green, 4 red; 3 blue, 6 red; 3 red, 1 green, 14 blue; 6 blue, 8 red; 15 blue, 9 red; 4 blue, 2 red
Game 93: 3 blue, 17 red, 2 green; 9 blue, 6 red; 6 blue, 2 green, 16 red; 1 green, 5 blue, 15 red; 3 blue, 2 green, 14 red
Game 94: 7 blue, 19 green, 1 red; 4 blue; 8 blue, 3 red, 4 green
Game 95: 2 green, 6 red, 13 blue; 5 red, 12 green, 12 blue; 18 blue, 8 red, 4 green; 7 red, 6 green, 17 blue; 4 green, 9 red, 6 blue; 10 red, 1 green, 4 blue
Game 96: 8 blue, 9 red; 9 red, 10 blue; 5 blue, 1 green, 2 red; 2 blue, 2 red
Game 97: 4 red, 1 blue, 2 green; 2 green, 11 red, 1 blue; 8 red, 1 green; 7 red, 3 green, 1 blue; 5 red, 1 green, 1 blue
Game 98: 6 green, 4 blue, 12 red; 3 blue, 13 red, 1 green; 2 blue, 12 green, 2 red; 13 green, 2 red, 1 blue; 10 red, 7 green, 1 blue
Game 99: 6 blue, 3 green, 5 red; 3 green, 6 red, 8 blue; 3 green, 11 blue, 14 red; 14 red, 5 green, 1 blue
Game 100: 16 red, 3 blue; 2 red, 5 green; 9 red; 1 blue, 3 green, 10 red; 1 red, 5 blue, 3 green; 12 blue, 9 red
"""
if __name__ == '__main__':
    
    # Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
    # What is the sum of the IDs of those games?
    # waht is the power of the bag?
    max_colors = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    print(sum_and_power_of_possible_games(games, max_colors))
    