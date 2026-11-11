# INF201 - Deliverable 3
# Based on game_simulator_v1.py by Turid Torheim (NMBU, 2026)


class Character:
    """A character in the RPG game."""

    # Added an optional weapon to the original constructor.
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon=None):
        # Added a check so maximum HP cannot be less than 1.
        if hp_max < 1:
            raise ValueError("Max HP must be at least 1")
        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon  # New attribute for an equipped weapon.

    @property
    def hp(self):
        return self._hp

    # New read-only property to check if the character is alive.
    @property
    def is_alive(self):
        return self._hp > 0

    # New method for taking damage without going below 0 HP.
    def take_damage(self, amount):
        self._hp = max(0, self._hp - max(0, amount))

    # New method for healing without going above maximum HP.
    def heal(self, amount):
        self._hp = min(self.hp_max, self._hp + max(0, amount))

    # Updated attack to support weapons.
    def attack(self, target):
        # Use base damage if no weapon is equipped.
        if self.weapon is None:
            damage = self.damage
        else:
            damage = self.weapon.roll_damage()  # Roll weapon damage.
        # Call take_damage() instead of changing target._hp directly.
        target.take_damage(damage)

    def introduce(self):
        print(f"Hi, my name is {self.name}!")

    # Updated the original __repr__ to show the character values clearly.
    def __repr__(self):
        return f"Character(name={self.name}, hp={self.hp}, damage={self.damage})"

    def __str__(self):
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"


# New Warrior subclass, not present in Turid's original file.
class Warrior(Character):
    """A character with armor."""

    def __init__(self, name, hp_max=100, damage=10, weapon=None, armor=5):
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor  # Task 4: Added armor (default 5).

    # Armor reduces damage before HP is changed.
    def take_damage(self, amount):
        damage = max(0, amount - self.armor)
        super().take_damage(damage)


#  New Mage subclass, not present in Turid's original file.
class Mage(Character):
    """A character that can use magic."""

    def __init__(self, name, hp_max=100, damage=10, weapon=None,
                 mana=30, mana_max=30):
        super().__init__(name, hp_max, damage, weapon)
        #  Added mana and maximum mana (default 30).
        self.mana_max = mana_max
        self.mana = min(mana, mana_max)

    # Mage has a special attack that uses mana.
    def attack(self, target):
        if self.mana >= 10:
            # Spend 10 mana and deal double base damage.
            self.mana -= 10
            target.take_damage(self.damage * 2)  # Magic ignores weapons
        else:
            # Without enough mana, use a normal attack and restore 5 mana.
            super().attack(target)  # Normal attack (uses weapon if equipped)
            self.mana = min(self.mana_max, self.mana + 5)
