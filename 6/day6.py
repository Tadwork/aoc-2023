#Part 1

def parse_input(text):
    lines = text.split('\n')
    times = [int(time) for time in lines[0].split(':')[1].strip().split()]
    distances = [int(distance) for distance in lines[1].split(':')[1].strip().split()]
    return zip(times, distances)

def number_of_ways_to_beat_record(scoreboard):
    records_broken = []
    for time, distance in scoreboard:
        records = 0
        for hold in range(time):
            if hold * (time - hold) > distance:
                records+=1
        records_broken.append(records)
    prod = 1
    for record in records_broken:
        prod *= record
    return prod

def parse_input_no_kerning(text):
    lines = text.split('\n')
    times = [int(lines[0].split(':')[1].strip().replace(' ',''))]
    distances = [int(lines[1].split(':')[1].strip().replace(' ',''))]
    return zip(times, distances)

if __name__ == '__main__':
    with open('6/input.txt') as f:
        text = f.read()
        scoreboard = parse_input(text)
        print(number_of_ways_to_beat_record(scoreboard))
        scoreboard_no_kerning = parse_input_no_kerning(text)
        print(number_of_ways_to_beat_record(scoreboard_no_kerning))
        
    