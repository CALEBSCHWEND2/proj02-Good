
# Part 2: Finding and Using Keys

In this part, you'll enhance the game by introducing keys that the player must find to unlock specific rooms. The player will explore the house, find hidden keys, and use them to unlock access to other rooms and eventually escape.

This part builds directly on the room navigation you completed in Part 1. You may continue from your own Part 1 solution or copy the instructor solution for Part 1 posted in D2L.

If you use the instructor solution, you are still responsible for understanding and explaining your final code.

Keys will be collected automatically when you visit specific rooms. You will also define all the rooms in the house in a list called `rooms`, and the keys (`key1` and `key2`) will be tracked using global variables so they can be accessed and modified from anywhere in the game.

## Requirements and Goals
- Define two keys tracked by `key1` and `key2`. In the game, these correspond to **Key 1**, which unlocks `Bathroom` and is collected in `Hallway`, and **Key 2**, which unlocks `Outside` and is collected in `Bathroom`.
- Display a message when the player picks up a key, including the key's name.
- Finish the game and print a message when the player escapes.
 
From Part 1:
- Allow the player to move between the rooms by typing directions (`d`, `s`, `w`, `a`).
- Display the player's current location after every move, and provide them with the available directions.
- Keep `get_directions(location)` as a helper that returns the directions string, and let `game_loop()` print `You can go: ...`.

## House Map

This is the updated map. In this map, we have a new location called `Outside`, which is the final location where the player can reach only after collecting all necessary keys and escaping.

- The `X` in the diagram below represents that the room is locked and requires a key to access it.
- **Key 1**: Found in the `Hallway`. Unlocks access to the `Bathroom`.
- **Key 2**: Found in the `Bathroom`. Unlocks the final exit to the `Outside`.

```
            |----------|-----------|
(unlock w/  |          | (unlock w/| 
    Key 2)  |          |   Key 1)  | 
    Outside | Bedroom  X Bathroom  | 
            |          |   *Key 2* |
  |----X----|---    ---|-----------|
  |         |          |
  | Kitchen   Hallway  | 
  |         |   *Key 1*| 
  |---------|----------|
```

### Example Flow
- The player starts in the `Bedroom`.
- The player tries to move to the `Bathroom`, but is denied since **Key 1** was not collected.
- The player moves to the `Hallway` and finds **Key 1**.
- Using **Key 1**, the player can enter the Bathroom and find **Key 2**.
- With both keys in hand, the player moves through the `Kitchen` and `Hallway` to reach the `Outside` and escape.

## Getting Started

- Open `escape.py` to start working on the project.

## How to Run
- Run the script directly in your terminal with `python escape.py` to see the output.

## Inputs
- Directions for movement:
  - `d` (right)
  - `s` (down)
  - `w` (up)
  - `a` (left)
- Exit the game:
  - `x` (ends the game)

- Keys will be picked up automatically when entering the corresponding room.


## What You Need to Implement

Starting from your Part 1 code or the instructor Part 1 solution posted in D2L, make the following Part 2 changes:

 - Implement function `def has_key_for_room(destination_room):` Check if the player has the key to enter a specified room, e.g. if `key1` is `True` to access `Bathroom`, or if `key2` is `True` to access `Outside`.

 - Implement function `def explore_room(location):` Handle picking up objects in the current room. This function checks the player's current location and updates the status of keys found in specific rooms. If the player is in the `Hallway` and hasn't picked up `key1` (`key1 == False`) yet, the function will mark `key1` as found and notify the player with the message `You found Key 1`. Similarly, if the player is in the `Bathroom` and hasn't picked up `key2` yet, the function will mark `key2` as found and notify the player with the message `You found Key 2`.

- Modify the `game_loop()` function to add the checks to either allow or deny the player to change to the `next_room`, depending on whether they have the key to enter the room.

As in Part 1, `get_directions(location)` should return the available directions text (for example, `d, s`), and `game_loop()` should print `You can go: ...` using that returned value.

## Expected Output
When you run your program, the console should display the following text exactly:

```
   Escape Game
   You are in the Bedroom.
   You can go: d, s
   Where do you want to go? ('x' to exit)
``` 
If the player types `d`, the game should display:
``` 
   You don't have the key to enter this room.
   You are in the Bedroom.
   You can go: d, s
   Where do you want to go? ('x' to exit)
```
If the player types `s`, the game should display:
``` 
   You are in the Hallway.
   You found Key 1
   You can go: w, a
   Where do you want to go? ('x' to exit)
```

If the player is in the `Kitchen` and types `w`, trying to go `Outside` without collecting **Key 2**, the game should display:
```
   You don't have the key to enter this room.
   You are in the Kitchen.
   You can go: d, w
   Where do you want to go? ('x' to exit)
```
- If the player is in `Bedroom` and types `d` with **Key 1** collected, the game should display:
```
   You are in the Bathroom.
   You found Key 2
   You can go: a
```
- If the player types `k` (which is an invalid direction), the game should display:
```
   Invalid direction. Try again.
   You are in the Bathroom.
   You can go: a
   Where do you want to go? ('x' to exit)
```

- If the player collected the 2 keys, is in the `Kitchen` and types `w`, the game should display:
```
   You have escaped!
```

If the player types `x`, the game exits, and the game should display:
``` 
   Exited the game.
``` 

## Assignment Completion Procedures

You will complete and submit this assignment in a similar way to prior
assignments. To avoid cluttering up this README with the same instructions each
time, they have been broken out into a separate file. Please reference
[PROCEDURES.md](PROCEDURES.md) to see the details if you have forgotten.

In summary:

  1.  Complete the code for the assignment per the instructions
  2.  Run the script to test and debug
  3.  Execute the automated tests to ensure expected functionality

When finished, do not forget to:

  1.  Commit and Sync:
      - Switch to version control tab
      - Stage all changed files
      - _**Enter a commit message**_
      - Click Commit
      - Click Sync
  2. Validate your submission in GitHub
