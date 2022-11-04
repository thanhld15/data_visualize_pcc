import pygal
import matplotlib.pyplot as plt

from dice import Dice

# Create a six-sided dice
dice1 = Dice()
dice2 = Dice(10)

# Make some rolls, and store values to a list
results = []
for _ in range(50000):
    result = dice1.roll() + dice2.roll()
    results.append(result)

# Analyze the result
frequencies = []
max_result = dice1.num_sides + dice2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the result
hist = pygal.Bar()
x_label = [str(total) for total in range(2, max_result+1)]

hist.title = "Histogram of rolling a D6 and a D10 50000 times"
hist.x_labels = x_label
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('../Image/double_dice_visual.svg')