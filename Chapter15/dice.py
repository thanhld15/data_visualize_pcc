from random import randint

class Dice():
    """A class simulate a normal dice"""

    def __init__(self, num_sides=6):
        """Assume a normal six-sided dice"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random number from 1 to num_sides"""
        return randint(1,self.num_sides)