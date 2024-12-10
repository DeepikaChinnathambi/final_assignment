import random

class Room:
    # Constants for room contents
    ITEMS = ['Healing Potion', 'Pit', 'Vision Potion', 'Pillar of OO', 'Entrance', 'Exit', 'None']

    def __init__(self, row, col):
        """Initialize room with row, column, and random contents."""
        self._row = row
        self._col = col
        self._contents = self._randomize_contents()
        self._items = {
            'Healing Potion': False,
            'Pit': False,
            'Vision Potion': False,
            'Pillar of OO': None,
            'Entrance': False,
            'Exit': False
        }

    def _randomize_contents(self):
        """Randomly assign items to the room ."""
        room_contents = {}
        if random.random() < 0.1:  # 10% chance for healing potion
            room_contents['Healing Potion'] = True
        if random.random() < 0.1:  # 10% chance for vision potion
            room_contents['Vision Potion'] = True
        if random.random() < 0.1:  # 10% chance for pit
            room_contents['Pit'] = True
        if random.random() < 0.05:  # 5% chance for Pillar of OO
            room_contents['Pillar of OO'] = random.choice(
                ['Abstraction', 'Encapsulation', 'Inheritance', 'Polymorphism'])
        if random.random() < 0.01:  # 1% chance for entrance
            room_contents['Entrance'] = True
        if random.random() < 0.01:  # 1% chance for exit
            room_contents['Exit'] = True
        return room_contents

    def get_contents(self):
        """Get the current contents of the room (encapsulation)"""
        return self._contents

    def __str__(self):
        """Return the graphical representation of the room."""
        north_south = "*----*"
        room_str = north_south + '\n'

        # Add room content in the center
        if self._contents.get('Exit'):
            room_str += "| {}  |".format('O')  # Exit
        elif self._contents.get('Entrance'):
            room_str += "| {}  |".format('i')  # Entrance
        elif self._contents.get('Pillar of OO'):
            room_str += "| {}  |".format(self._contents['Pillar of OO'][0])  # First letter of Pillar type
        elif self._contents.get('Healing Potion'):
            room_str += "| {}  |".format('H')  # Healing Potion
        elif self._contents.get('Vision Potion'):
            room_str += "| {}  |".format('V')  # Vision Potion
        elif self._contents.get('Pit'):
            room_str += "| {}  |".format('P')  # Pit
        else:
            room_str += "| {}  |".format(' ')  # Empty room

        room_str += '\n' + north_south
        return room_str

    def trigger_event(self, adventurer):
        """Triggers the event of interacting with the room."""
        if self._contents.get('Healing Potion'):
            adventurer.healing_potions += 1
            self._contents['Healing Potion'] = False  # Remove the potion from the room
        if self._contents.get('Vision Potion'):
            adventurer.vision_potions += 1
            self._contents['Vision Potion'] = False  # Remove the potion from the room
        if self._contents.get('Pit'):
            damage = random.randint(1, 20)
            adventurer.hit_points -= damage
            self._contents['Pit'] = False  # Remove the pit from the room
        if self._contents.get('Pillar of OO'):
            pillar = self._contents['Pillar of OO']
            adventurer.pillars_found.append(pillar)
            self._contents['Pillar of OO'] = None  # Remove the pillar from the room
        if self._contents.get('Exit'):
            # If adventurer reaches the exit, trigger win condition (game logic handled elsewhere)
            pass

    def has_door(self, direction):
        """Check if the room has a door in a given direction (N, S, E, W)."""
        return direction in self._contents and self._contents[direction]
