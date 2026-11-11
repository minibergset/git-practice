import random


class Dice:
    def __init__(self, sides=6):
        # Any number of sides >= 2; default is 6.
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides")
        self.sides = sides

    def roll(self):
        # Roll a random number from 1 to sides.
        return random.randint(1, self.sides)

    def __repr__(self):
        # Show the dice as Dice(sides=6).
        return f"Dice(sides={self.sides})"

    def __call__(self):
        # Allow d20() to roll the dice, like d20.roll().
        return self.roll()
