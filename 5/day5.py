from tqdm import tqdm

class InstructionRange():
    def __init__(self) -> None:
        self.ranges = {}
    def add(self,source_start, dest_start,length):
        self.ranges[source_start] = {'dest_start':dest_start,'length':length}
    
    def get(self, source):
        for start,rng in self.ranges.items():
            if source >= start and source < start + rng['length']:
                return source - start + rng['dest_start']
        return source
    

class Almanac:
    seeds = []
    min_valid_seed = float('inf')
    max_valid_seed = 0
    seed_to_soil = InstructionRange()
    soil_to_fertilizer = InstructionRange()
    fertilizer_to_water = InstructionRange()
    water_to_light = InstructionRange()
    light_to_temperature = InstructionRange()
    temperature_to_humidity = InstructionRange()
    humidity_to_location = InstructionRange()
    
    soil_to_seed = InstructionRange()
    fertilizer_to_soil = InstructionRange()
    water_to_fertilizer = InstructionRange()
    light_to_water = InstructionRange()
    temperature_to_light = InstructionRange()
    humidity_to_temperature = InstructionRange()
    location_to_humidity = InstructionRange()
    
    
    def __init__(self, input:str) -> None:
        lines = input.splitlines()
        line_num = 0
        while line_num < len(lines):
            line = lines[line_num].strip()
            if not line:
                line_num+=1
                continue
            if line.startswith('seeds:'):
                seed_list = line.split(':')[1].strip().split()
                seed_iter = iter(seed_list)
                for seed in seed_iter:
                    length = int(next(seed_iter))
                    self.min_valid_seed = min(self.min_valid_seed, int(seed))
                    self.max_valid_seed = max(self.max_valid_seed, int(seed) + length)
                    self.seeds.append({ 'seed':int(seed), 'length':length})
            elif 'map' in line:
                src_name,_,dest_name = line.split()[0].split('-')
                prop = getattr(self,f'{src_name}_to_{dest_name}')
                rev_prop = getattr(self,f'{dest_name}_to_{src_name}')
                line_num+=1
                while line_num < len(lines) and lines[line_num].strip():
                    dest,source,count = lines[line_num].split()
                    prop.add(int(source), int(dest), int(count))
                    rev_prop.add(int(dest), int(source), int(count))
                    line_num+=1
            line_num+=1
            
    def get_location(self,seed):
        soil = self.seed_to_soil.get(seed)
        fertilizer = self.soil_to_fertilizer.get(soil)
        water = self.fertilizer_to_water.get(fertilizer)
        light = self.water_to_light.get(water)
        temperature = self.light_to_temperature.get(light)
        humidity = self.temperature_to_humidity.get(temperature)
        location = self.humidity_to_location.get(humidity)
        return location
    
    def get_seed(self,location):
        humidity = self.location_to_humidity.get(location)
        temperature = self.humidity_to_temperature.get(humidity)
        light = self.temperature_to_light.get(temperature)
        water = self.light_to_water.get(light)
        fertilizer = self.water_to_fertilizer.get(water)
        soil = self.fertilizer_to_soil.get(fertilizer)
        seed = self.soil_to_seed.get(soil)
        return seed
    
    def is_valid_seed(self,seed):
        if seed < self.min_valid_seed or seed > self.max_valid_seed:
            return False
        for s in self.seeds:
            if s['seed'] <= seed <= s['seed'] + s['length']:
                return True
        return False
    
    def find_min_location(self):
        known_valid_min_location = min(self.location_to_humidity.ranges.keys())
        for location in tqdm(range(1,known_valid_min_location)):
            seed = self.get_seed(location)
            if self.is_valid_seed(seed):
                return location
    
if __name__ == '__main__':
    with open('5/almanac.txt',mode='r', encoding='utf-8') as f:
        almanac = Almanac(f.read())
        print(almanac.find_min_location())