import pygal

from dice import Dice

# Create a six-sided dice
dice = Dice()

# Make some rolls, and store values to a list
results = []
for _ in range(1000):
    result = dice.roll()
    results.append(result)

# Analyze the result
frequencies = []
for value in range(1,dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the result
hist = pygal.Bar()

hist.title = "Histogram of rolling a D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('../Image/dice_visual.svg')