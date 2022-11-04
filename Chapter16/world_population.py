import json
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code

filename = './data/population_data.json'

# Read the population data file
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data
cc_pop_1, cc_pop_2, cc_pop_3 = {},{},{}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        code = get_country_code(country_name=country_name)
        if code:
            population = int(float(pop_dict['Value']))
            if population < 10000000:
                cc_pop_1[code] = population
            elif population < 1000000000:
                cc_pop_2[code] = population
            else:
                cc_pop_3[code] = population

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = "World populations in 2020, by Country"
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('world_population.svg')