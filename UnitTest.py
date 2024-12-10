import unittest
from unittest.mock import patch
from Room import Room
from Adventurer import Adventurer
from Dungeon import Dungeon


class TestAdventure(unittest.TestCase):

    def setUp(self):
        # Assuming you have an Adventurer class and a Dungeon class
        self.dungeon = Dungeon(4,4)  # Initialize Dungeon (Assumed class)
        self.adventurer = Adventurer("Test_Adventure")  # Initialize Adventurer (Assumed class)
        entrance = self.dungeon.get_entrance()
        self.adventurer.position = (entrance._row, entrance._col)  # Set initial position to entrance

    def test_move_adventurer_invalid(self):
        initial_position = self.adventurer.position
        # Try an invalid move (e.g., move North when there is a wall)
        self.dungeon.move_adventurer(self.adventurer, 'North')
        # The position should not change if the move is invalid
        self.assertEqual(initial_position, self.adventurer.position)

    def test_move_adventurer_valid(self):
        initial_position = self.adventurer.position
        # Try a valid move (e.g., move South)
        self.dungeon.move_adventurer(self.adventurer, 'South')
        # The position should change
        self.assertNotEqual(initial_position, self.adventurer.position)

    @patch('random.choice', return_value='South')
    def test_move_adventurer_random(self, mock_random):
        initial_position = self.adventurer.position
        self.dungeon.move_adventurer(self.adventurer, 'South')
        self.assertNotEqual(initial_position, self.adventurer.position)

    def test_pillar_collection(self):
         room = self.dungeon.get_room(1, 1)  # Access a specific room
         room._contents['Pillar of OO'] = 'Abstraction'  # Mock room with pillar
         self.adventurer.position = (1, 1)  # Place adventurer in the room
         room.trigger_event(self.adventurer)  # Trigger event
         self.assertIn("Abstraction", self.adventurer.pillars_found)

    def test_dungeon_display(self):
        with patch("builtins.print") as mock_print:
            self.dungeon.display()
            mock_print.assert_called()  # Check if display method was called


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.dungeon = Dungeon(4, 4)
        self.adventurer = Adventurer("Test_Adventure")
        entrance = self.dungeon.get_entrance()
        self.adventurer.position = (entrance._row, entrance._col)

    def test_initialization(self):
        self.assertEqual(len(self.dungeon._grid), 4)  # Check rows
        self.assertEqual(len(self.dungeon._grid[0]), 4)  # Check columns
        self.assertIsNotNone(self.dungeon.get_entrance())
        self.assertIsNotNone(self.dungeon.get_exit())

    def test_move_adventurer_valid(self):
        initial_position = self.adventurer.position
        # Assume there's no wall or check if there's a valid room in the south
        self.dungeon.move_adventurer(self.adventurer, 'South')
        # Assert that position has changed if the move was valid
        self.assertNotEqual(initial_position, self.adventurer.position)

    def test_move_adventurer_invalid(self):
        # Try moving outside the dungeon bounds
        initial_position = self.adventurer.position
        self.dungeon.move_adventurer(self.adventurer, 'North')
        self.assertEqual(initial_position, self.adventurer.position)

    @patch('random.choice', return_value='South')
    def test_move_adventurer_random(self, mock_random):
        initial_position = self.adventurer.position
        self.dungeon.move_adventurer(self.adventurer, 'South')
        # Assert that position has changed
        self.assertNotEqual(initial_position, self.adventurer.position)


    def test_pillar_collection(self):
        # Set a pillar in a room (make sure the room is not empty)
        room = self.dungeon.get_room(1, 1)  # Access a room directly (make sure the room exists)
        room._contents['Pillar of OO'] = 'Abstraction'  # Mock the room having a pillar

        # Move the adventurer to the room where the pillar is located
        self.dungeon.move_adventurer(self.adventurer, 'South')  # Move adventurer to the correct room

        # Make sure the adventurer collects the pillar
        self.assertIn("Abstraction", self.adventurer.pillars_found)

    def test_dungeon_display(self):
        with patch("builtins.print") as mock_print:
            self.dungeon.display()
            # Check if dungeon layout is printed
            mock_print.assert_called()

    def test_game_ending(self):
        # Collect all the pillars
        self.adventurer.add_pillar("Abstraction")
        self.adventurer.add_pillar("Encapsulation")
        self.adventurer.add_pillar("Inheritance")
        self.adventurer.add_pillar("Polymorphism")

        # Make the adventurer lose all HP
        self.adventurer.take_damage(100)

        # HP should not go below 0
        self.assertEqual(self.adventurer.hit_points, 0)

        # Test if adventurer loses after HP reaches 0
        self.adventurer.take_damage(100)
        self.assertEqual(self.adventurer.hit_points, 0)

if __name__ == '__main__':
    unittest.main()
