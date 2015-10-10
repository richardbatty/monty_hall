import unittest
from lib.game import Game
from lib.door import Door

class GameTest(unittest.TestCase):

    def test_first_round(self):
        door_1, door_2, door_3 = Door('goat'), Door('goat'), Door('car')
        game = Game(door_1, door_2, door_3)
        game.contestant_guess = 0
        game.host_open_door()
        self.assertEqual(True, door_2.is_open)

    def test_different_first_round(self):
        door_1, door_2, door_3 = Door('goat'), Door('car'), Door('goat')
        game = Game(door_1, door_2, door_3)
        game.contestant_guess = 0
        game.host_open_door()
        self.assertEqual(True, door_3.is_open)

# game = Game('goat', 'goat', 'car')
# contestant = Contestant(guess_strategy, stick_or_switch_strategy)
# game.contestant_guess(contestant.guess)
# game.host_open_door()
# game.contestant_stick_or_switch(contestant.stick_or_switch)
# game.contestant_open_door()
# game.result()
