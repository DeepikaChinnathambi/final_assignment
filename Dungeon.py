import random
from Room import Room

class Dungeon:
    def __init__(self, rows, cols):
        """
        Initialize the dungeon grid with the given number of rows and columns.
        """
        self._rows = rows
        self._cols = cols
        self._grid = [[Room(row, col) for col in range(cols)] for row in range(rows)]
        self._entrance = None
        self._exit = None
        self._place_special_rooms()

    def _place_special_rooms(self):
        """
        Randomly assign entrance, exit, and Pillars of OO to rooms.
        """
        # Choose random locations for the Entrance and Exit
        entrance_coords = self._random_coords()
        exit_coords = self._random_coords(exclude=entrance_coords)

        # Set the entrance and exit
        self._entrance = self._grid[entrance_coords[0]][entrance_coords[1]]
        self._entrance._contents['Entrance'] = True

        self._exit = self._grid[exit_coords[0]][exit_coords[1]]
        self._exit._contents['Exit'] = True

        # Place the Pillars of OO in distinct random rooms
        pillars = ['Abstraction', 'Encapsulation', 'Inheritance', 'Polymorphism']
        for pillar in pillars:
            while True:
                pillar_coords = self._random_coords(exclude=[entrance_coords, exit_coords])
                room = self._grid[pillar_coords[0]][pillar_coords[1]]
                if not room._contents.get('Pillar of OO'):  # Ensure no other pillar is in the room
                    room._contents['Pillar of OO'] = pillar
                    break

    def _random_coords(self, exclude=None):
        """
        Generate random coordinates for a room in the dungeon, avoiding any in the 'exclude' list.
        """
        exclude = exclude or []
        while True:
            row = random.randint(0, self._rows - 1)
            col = random.randint(0, self._cols - 1)
            if (row, col) not in exclude:
                return (row, col)

    def get_room(self, row, col):
        """
        Return the room at the specified row and column.
        """
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self._grid[row][col]
        return None

    def display(self):
        """
        Display a simple representation of the dungeon layout.
        """
        for row in self._grid:
            print(" | ".join(str(room) for room in row))
            print("-" * (self._cols * 7))  # Adjusted for formatting

    def move_adventurer(self, adventurer, direction):
        """
        Move the adventurer in the specified direction if possible.
        """
        current_row, current_col = adventurer.position
        new_row, new_col = current_row, current_col

        if direction == 'North':
            new_row -= 1
        elif direction == 'South':
            new_row += 1
        elif direction == 'East':
            new_col += 1
        elif direction == 'West':
            new_col -= 1

        # Check if the new position is valid
        new_room = self.get_room(new_row, new_col)
        if new_room:
            adventurer.position = (new_row, new_col)
            print(f"{adventurer.name} moved {direction} to Room ({new_row}, {new_col}).")
            new_room.trigger_event(adventurer)
        else:
            print(f"Cannot move {direction}. There is a wall.")

    def get_entrance(self):
        """
        Return the entrance room.
        """
        return self._entrance

    def get_exit(self):
        """
        Return the exit room.
        """
        return self._exit
