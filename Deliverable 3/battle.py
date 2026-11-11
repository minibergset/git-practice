from game_simulator_v2 import Character


class Battle:
    def __init__(self, hero: Character, enemy: Character):
        # Store the two characters in the battle.
        self.hero = hero
        self.enemy = enemy

    def play_round(self):
        # Hero attacks first.
        self.hero.attack(self.enemy)
        # Enemy attacks only if still alive.
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self):
        # Repeat rounds until one character is dead.
        round_number = 0
        while self.hero.is_alive and self.enemy.is_alive:
            round_number += 1
            self.play_round()
            print(f"Round {round_number}: {self.hero.name} {self.hero.hp} HP, "
                  f"{self.enemy.name} {self.enemy.hp} HP")

        if self.hero.is_alive:
            winner = self.hero
        else:
            winner = self.enemy
        print("Winner:", winner.name)
        return winner
