from dice import Dice


class Weapon:
    def __init__(self, name: str, damage_dice: Dice):
        #  A weapon has a name and a Dice object.
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self):
        #  Roll the weapon's dice to calculate damage.
        return self.damage_dice.roll()
