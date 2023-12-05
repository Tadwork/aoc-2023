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
    seed_to_soil = InstructionRange()
    soil_to_fertilizer = InstructionRange()
    fertilizer_to_water = InstructionRange()
    water_to_light = InstructionRange()
    light_to_temperature = InstructionRange()
    temperature_to_humidity = InstructionRange()
    humidity_to_location = InstructionRange()
    
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
                    self.seeds.append({ 'seed':int(seed), 'length':int(next(seed_iter))})
            elif 'map' in line:
                property_name = line.split()[0].replace('-','_')
                prop = getattr(self,property_name)
                line_num+=1
                while line_num < len(lines) and lines[line_num].strip():
                    dest,source,count = lines[line_num].split()
                    prop.add(int(source), int(dest), int(count))
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
    
    def find_min_location(self):
        locations = []
        for seed in self.seeds:
            for seed_location in range(seed['seed'],seed['seed']+seed['length']):
                locations.append(self.get_location(seed_location))
        return min(locations)
    
if __name__ == '__main__':
    with open('5/almanac.txt',mode='r', encoding='utf-8') as f:
        almanac = Almanac(f.read())
        print(almanac.find_min_location())