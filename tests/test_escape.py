import unittest
from unittest.mock import patch
from io import StringIO
import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from escape import (
    print_location,
    get_directions,
    find_room_by_direction,
    explore_room,
    has_key_for_room,
    game_loop,
    start_game,
)

class TestEscapeGame(unittest.TestCase):

    def setUp(self):
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout
        # Patch key1 and key2 in the escape module before each test
        self.patcher_key1 = patch('escape.key1', False)
        self.patcher_key2 = patch('escape.key2', False)
        self.mock_key1 = self.patcher_key1.start()
        self.mock_key2 = self.patcher_key2.start()
    
    def tearDown(self):
        # Stop patching key1 and key2 after each test
        self.patcher_key1.stop()
        self.patcher_key2.stop()
        self.held_stdout.close()
        sys.stdout = sys.__stdout__

    def reset_stdout(self):
        self.held_stdout.truncate(0)
        self.held_stdout.seek(0)

    def make_mock_input(self, responses):
        responses = iter(responses)

        def _mock_input(prompt=""):
            print(prompt.rstrip())
            return next(responses)

        return _mock_input

    def test_print_location_bedroom(self):
        print_location("Bedroom")
        self.assertEqual(self.held_stdout.getvalue(), "You are in the Bedroom.\n")

    def test_print_location_unknown(self):
        self.reset_stdout()
        print_location("Unknown")
        self.assertEqual(self.held_stdout.getvalue(), "Unknown location.\n")

    def test_get_directions_bedroom(self):
        self.assertEqual(get_directions("Bedroom"), "d, s")

    def test_get_directions_kitchen(self):
        self.assertEqual(get_directions("Kitchen"), "d, w")

    def test_find_room_by_direction_bedroom_to_bathroom(self):
        self.assertEqual(find_room_by_direction("Bedroom", "d"), "Bathroom")

    def test_find_room_by_direction_hallway_to_kitchen(self):
        self.assertEqual(find_room_by_direction("Hallway", "a"), "Kitchen")

    def test_find_room_by_direction_kitchen_to_outside(self):
        self.assertEqual(find_room_by_direction("Kitchen", "w"), "Outside")

    def test_find_room_by_direction_invalid(self):
        self.assertEqual(find_room_by_direction("Bedroom", "x"), "Bedroom")  # Invalid direction
        self.assertEqual(self.held_stdout.getvalue(), "Invalid direction. Try again.\n")

    def test_startup_and_exit_transcript(self):
        """Test the exact startup and exit transcript."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=self.make_mock_input(['x'])):
                start_game()
                game_loop("Bedroom")
            output = fake_out.getvalue()
            self.assertEqual(
                output,
                "Escape Game\n"
                "You are in the Bedroom.\n"
                "You can go: d, s\n"
                "Where do you want to go? ('x' to exit)\n"
                "Exited the game.\n",
            )

    def test_cannot_enter_locked_room_without_key_transcript(self):
        """Test the exact transcript when the player tries a locked room first."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=self.make_mock_input(['d', 'x'])):
                start_game()
                game_loop("Bedroom")
            output = fake_out.getvalue()
            self.assertEqual(
                output,
                "Escape Game\n"
                "You are in the Bedroom.\n"
                "You can go: d, s\n"
                "Where do you want to go? ('x' to exit)\n"
                "You don't have the key to enter this room.\n"
                "You are in the Bedroom.\n"
                "You can go: d, s\n"
                "Where do you want to go? ('x' to exit)\n"
                "Exited the game.\n",
            )

    def test_key1_pickup_transcript(self):
        """Test the exact transcript when the player finds Key 1."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with patch('builtins.input', side_effect=self.make_mock_input(['s', 'x'])):
                start_game()
                game_loop("Bedroom")
            output = fake_out.getvalue()
            self.assertEqual(
                output,
                "Escape Game\n"
                "You are in the Bedroom.\n"
                "You can go: d, s\n"
                "Where do you want to go? ('x' to exit)\n"
                "You are in the Hallway.\n"
                "You found Key 1\n"
                "You can go: w, a\n"
                "Where do you want to go? ('x' to exit)\n"
                "Exited the game.\n",
            )

    def test_explore_room_hallway(self):
        explore_room("Hallway")
        self.assertEqual(self.held_stdout.getvalue(), "You found Key 1\n")

    def test_explore_room_bathroom(self):
        explore_room("Bathroom")
        self.assertEqual(self.held_stdout.getvalue(), "You found Key 2\n")

    def test_has_key_for_room_bathroom_no_key(self):
        self.assertFalse(has_key_for_room("Bathroom"))

    def test_has_key_for_room_bathroom_with_key(self):
        with patch('escape.key1', True):
            self.assertTrue(has_key_for_room("Bathroom"))

    def test_has_key_for_room_outside_no_key(self):
        self.assertFalse(has_key_for_room("Outside"))

    def test_has_key_for_room_outside_with_key(self):
        with patch('escape.key2', True):
            self.assertTrue(has_key_for_room("Outside"))

if __name__ == "__main__":
    unittest.main()
