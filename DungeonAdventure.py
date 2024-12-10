import random
from Adventurer import Adventurer
from Dungeon import Dungeon


def main():
    # Create a dungeon
    dungeon = Dungeon(4, 4)

    # Create an adventurer
    adventurer = Adventurer("Test_Adventure")
    entrance = dungeon.get_entrance()
    adventurer.position = (entrance._row, entrance._col)  # Start at the entrance

    # Display the dungeon layout (for debugging purposes)
    print("Dungeon Layout:")
    dungeon.display()

    # Starting the adventure
    print("\nStarting Adventure!")
    commands = ['North', 'East', 'South', 'West']
    moves = 0
    while moves < 10:
        if adventurer.hit_points <= 0:
            print(f"{adventurer.name} has run out of HP and lost!")
            break

        # Move adventurer and interact with rooms
        direction = random.choice(commands)
        print(f"\nAttempting to move {direction}...")
        if dungeon.move_adventurer(adventurer, direction):
            moves += 1
            print(f"{adventurer.name} moved {direction} to Room {adventurer.position}")
        else:
            print(f"{adventurer.name} cannot move {direction}. There is a wall or invalid move.")

        # Check if adventurer has collected all Pillars of OO (Winning Condition)
        if len(adventurer.pillars_found) == 4:
            print(f"{adventurer.name} has collected all the Pillars of OO and won!")
            break

        # Show the adventurer's status after each move
        print(adventurer)

        # If the adventurer has lost all HP
        if adventurer.hit_points <= 0:
            print(f"{adventurer.name} has run out of HP and lost!")
            break

    # If all moves are used and conditions are not met, display a message
    if moves == 10 and len(adventurer.pillars_found) < 4 and adventurer.hit_points > 0:
        print(f"{adventurer.name} could not collect all the Pillars of OO in 10 moves. Game over!")

if __name__ == "__main__":
    main()
