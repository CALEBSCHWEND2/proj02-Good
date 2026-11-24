## Locations:
    # Bedroom
    # Hallway
    # Bathroom
    # Kitchen

# House map
#             |----------|-----------|
# (unlock w/  |          | (unlock w/|
#     Key 2)  |          |   Key 1)  |
#     Outside | Bedroom  X Bathroom  |
#             |          |   *Key 2* |
#   |----X----|---    ---|-----------|
#   |         |          |
#   | Kitchen   Hallway  |
#   |         |   *Key 1*|
#   |---------|----------|

## List of rooms
rooms = ["Bedroom", "Hallway", "Bathroom", "Kitchen", "Outside"]

## Key state (`key1` and `key2` are code variables, not display names)
key1 = False
key2 = False

START_LOCATION = "Bedroom"

def print_location(location: str) -> None:
    """
    Print the description of the current location.
    """
    if location in rooms:
        print(f"You are in the {location}.")
    else:
        print("Unknown location.")

def get_directions(location: str) -> str:
    """
    Return possible directions to move from the current location.
    """
    # Copy solution from Part 1 and update to add the outside location when in the kitchen.
    # Return strings such as "d, s" or "d, w" instead of printing them.
    if location == "Bedroom":
        return "d, s"
    elif location == "Hallway":
        return "w, a"
    elif location == "Bathroom":
        return "a"
    elif location == "Kitchen":
        return "d, w"
    else:
        return ""

def find_room_by_direction(location: str, direction: str) -> str:
    """
    Determine the new location based on the current location and direction.
    """
    # Copy solution from Part 1 and update it to handle the outside
    match(location):
        case("Bedroom"):
            match(direction):
                case("s"):
                    return "Hallway"
                case("d"):
                    return "Bathroom"
                case (_):
                    print("Invalid direction. Try again.")
                    return location
        case("Hallway"):
            match(direction):
                case("a"):
                    return "Kitchen"
                case("w"):
                    return "Bedroom"
                case (_):
                    print("Invalid direction. Try again.")
                    return location
        case("Bathroom"):
            match(direction):
                case("a"):
                    return "Bedroom"
                case (_):
                    print("Invalid direction. Try again.")
                    return location
        case("Kitchen"):
            match(direction):
                case("d"):
                    return "Hallway"
                case("w"):
                    return "Outside"
                case (_):
                    print("Invalid direction. Try again.")
                    return location
        case(_):
            return location


def has_key_for_room(destination_room: str) -> bool:
    """
    Check if the player has the required code-tracked key to enter a room.

    Args:
        destination_room (str): The identifier of the room to check.
                                Possible values are "Outside" and "Bathroom".

    Returns:
        bool: True if the player has the key to enter the room, False otherwise.

    Notes:
        - If the destination_room is "Outside", the function checks the global variable `key2`
          (which represents Key 2 in the game).
        - If the destination_room is "Bathroom", the function checks the global variable `key1`
          (which represents Key 1 in the game).
    """
    global key1
    global key2
    match(destination_room):
        case("Bathroom"):
            if not key1:
                print("You don't have the key to enter this room.")
            return key1
        case("Outside"):
            if not key2:
                print("You don't have the key to enter this room.")
            return key2
        case (_):
            return True


def explore_room(location: str) -> None:
    """
    Handle picking up objects in the current room.

    This function checks the player's current location and updates the status
    of keys found in specific rooms. If the player is in the "Hallway" and
    hasn't picked up `key1` yet, the function will mark `key1` as found and
    notify the player with the display message "You found Key 1". Similarly,
    if the player is in the "Bathroom" and hasn't picked up `key2` yet, the
    function will mark `key2` as found and notify the player with the display
    message "You found Key 2".

    Args:
        location (str): The current location of the player. Expected values
                        are "Hallway" or "Bathroom".

    Returns:
        None
    """
    global key1
    global key2
    if location == "Hallway" and not key1:
        print("You found Key 1")
        key1 = True
    elif location == "Bathroom" and not key2:
        print("You found Key 2")
        key2 = True

def game_loop(location: str) -> None:
    """
    Main game loop handling room navigation and key pickup.
    """

    while True:
        print_location(location)
        explore_room(location)

        available_directions = get_directions(location)
        print(f"You can go: {available_directions}")

        chosen_direction = input("Where do you want to go? ('x' to exit) ").strip().lower()

        if chosen_direction == 'x':
            break

        next_room = find_room_by_direction(location, chosen_direction)

        # Check whether the player can enter the destination room
        if has_key_for_room(next_room):
            location = next_room

        # Check whether the player escaped
        if location == "Outside":
            print("You have escaped!")
            return

    print("Exited the game.")


def start_game() -> None:
    """
    Start the game.

    This function initializes the Escape Game by printing the game title to the console.
    It serves as the entry point for the game.
    """

    print("Escape Game")

if __name__ == "__main__":
    start_game()
    game_loop(START_LOCATION)