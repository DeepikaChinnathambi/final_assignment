import random

class Adventurer:
    def __init__(self, name, hit_points=None):
        """Initialize adventurer with name, hit points, and items."""
        self.position = None
        self.name = name
        self.hit_points = hit_points if hit_points is not None else random.randint(75, 100)
        self.max_hit_points = self.hit_points  # Set max HP as the initial value
        self.healing_potions = 0
        self.vision_potions = 0
        self.pillars_found = []

    def add_healing_potion(self, amount):
        """
        Add healing potions to the adventurer's inventory and heal HP.

        Args:
            amount (int): The amount of HP to restore.
        """
        self.healing_potions += 1
        self.hit_points = min(self.hit_points + amount, self.max_hit_points)
        print(f"{self.name} healed {amount} HP. Current HP: {self.hit_points}")

    def take_damage(self, damage):
        """
        Reduce the adventurer's HP when they take damage.

        Args:
            damage (int): The amount of damage to deal.
        """
        self.hit_points -= damage
        if self.hit_points < 0:
            self.hit_points = 0  # Prevent HP from going below 0
        print(f"{self.name} took {damage} damage. Current HP: {self.hit_points}")

    def add_vision_potion(self):
        """Add vision potion to the adventurer's inventory."""
        self.vision_potions += 1
        print(f"{self.name} found a vision potion. Total: {self.vision_potions}")

    def add_pillar(self, pillar):
        """
        Add a Pillar of OO to the adventurer's collection.

        Args:
            pillar (str): The name of the pillar to add.
        """
        if pillar not in self.pillars_found:
            self.pillars_found.append(pillar)
            print(f"{self.name} collected the {pillar}.")
        else:
            print(f"{self.name} already has the {pillar}.")

    def __str__(self):
        """Return adventurer's current status."""
        pillars = ', '.join(self.pillars_found) if self.pillars_found else "None"
        return (f"{self.name}\nHP: {self.hit_points}\nHealing Potions: {self.healing_potions}"
                f"\nVision Potions: {self.vision_potions}\nPillars: {pillars}")
